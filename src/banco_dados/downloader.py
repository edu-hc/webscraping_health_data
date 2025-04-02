# Script para baixar dados da ANS
import os
import requests
import zipfile
import io
from datetime import datetime
import time
import re
from bs4 import BeautifulSoup

# Configurações iniciais
data_dir = "dados_ans"
os.makedirs(data_dir, exist_ok=True)


def baixar_demonstracoes_contabeis():
    """
    Baixa os arquivos de demonstrações contábeis dos últimos 2 anos do repositório da ANS.
    """
    print("Baixando demonstrações contábeis dos últimos 2 anos...")
    base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"

    # Criar diretório para demonstrações contábeis
    demo_dir = os.path.join(data_dir, "demonstracoes_contabeis")
    os.makedirs(demo_dir, exist_ok=True)

    # Obter a lista de arquivos disponíveis no repositório
    try:
        response = requests.get(base_url)
        response.raise_for_status()

        # Usar regex para encontrar arquivos ZIP de trimestrais (formato: AAAA_QT_DIOPS.zip)
        pattern = r'(\d{4})_(\d)T_DIOPS\.zip'
        matches = re.findall(pattern, response.text)

        # Alternativa usando BeautifulSoup se o regex não funcionar bem
        if not matches:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            matches = []
            for link in links:
                match = re.search(pattern, link['href'])
                if match:
                    matches.append((match.group(1), match.group(2)))

        # Filtrar para manter apenas os últimos 2 anos
        current_year = datetime.now().year
        last_two_years = [str(current_year - i) for i in range(2)]
        filtered_matches = [(year, trimester) for year, trimester in matches if year in last_two_years]

        print(f"Encontrados {len(filtered_matches)} arquivos dos últimos 2 anos para download.")

        # Baixar cada arquivo
        for year, trimester in filtered_matches:
            file_name = f"{year}_{trimester}T_DIOPS.zip"
            file_url = f"{base_url}{file_name}"
            download_path = os.path.join(demo_dir, file_name)

            print(f"Baixando {file_name}...")

            try:
                file_response = requests.get(file_url, stream=True)
                file_response.raise_for_status()

                # Salvar o arquivo ZIP
                with open(download_path, 'wb') as f:
                    for chunk in file_response.iter_content(chunk_size=8192):
                        f.write(chunk)

                print(f"Download completo: {file_name}")

                # Extrair o conteúdo do ZIP
                extract_dir = os.path.join(demo_dir, f"{year}_{trimester}T")
                os.makedirs(extract_dir, exist_ok=True)

                with zipfile.ZipFile(download_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_dir)

                print(f"Arquivo extraído em: {extract_dir}")

                # Pequena pausa para não sobrecarregar o servidor
                time.sleep(1)

            except Exception as e:
                print(f"Erro ao baixar ou extrair {file_name}: {e}")

        return True

    except Exception as e:
        print(f"Erro ao acessar o repositório de demonstrações contábeis: {e}")
        return False


def baixar_dados_operadoras():
    """
    Baixa os dados cadastrais das operadoras ativas da ANS.
    """
    print("\nBaixando dados cadastrais das operadoras ativas...")

    # URL do arquivo CSV das operadoras ativas
    url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_Cadop.csv"

    # Criar diretório para dados das operadoras
    op_dir = os.path.join(data_dir, "operadoras")
    os.makedirs(op_dir, exist_ok=True)

    # Caminho para salvar o arquivo
    save_path = os.path.join(op_dir, "operadoras_ativas.csv")

    try:
        # Verificar se o diretório existe
        op_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
        dir_response = requests.get(op_url)
        dir_response.raise_for_status()

        # Fazer o download do arquivo CSV
        print(f"Baixando arquivo: Relatorio_Cadop.csv")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Salvar o arquivo
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Download completo: {save_path}")

        # Verificar tamanho do arquivo para garantir que foi baixado corretamente
        file_size = os.path.getsize(save_path)
        print(f"Tamanho do arquivo: {file_size / (1024 * 1024):.2f} MB")

        return True

    except Exception as e:
        print(f"Erro ao baixar dados das operadoras: {e}")

        # Verificar se o arquivo existe na URL
        try:
            head_response = requests.head(url)
            if head_response.status_code != 200:
                print(f"O arquivo não está disponível na URL {url}. Status code: {head_response.status_code}")

                # Tentar listar diretório para encontrar o arquivo correto
                print("Tentando listar diretório para encontrar o arquivo correto...")
                base_dir = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
                try:
                    dir_response = requests.get(base_dir)
                    dir_response.raise_for_status()

                    # Procurar por arquivos CSV
                    soup = BeautifulSoup(dir_response.text, 'html.parser')
                    csv_links = [link['href'] for link in soup.find_all('a', href=True) if
                                 link['href'].endswith('.csv')]

                    if csv_links:
                        print(f"Arquivos CSV encontrados no diretório: {csv_links}")

                        # Tentar baixar o primeiro arquivo CSV encontrado
                        alt_url = base_dir + csv_links[0]
                        print(f"Tentando baixar arquivo alternativo: {alt_url}")

                        alt_response = requests.get(alt_url, stream=True)
                        alt_response.raise_for_status()

                        # Salvar o arquivo alternativo
                        alt_path = os.path.join(op_dir, csv_links[0])
                        with open(alt_path, 'wb') as f:
                            for chunk in alt_response.iter_content(chunk_size=8192):
                                f.write(chunk)

                        print(f"Download alternativo completo: {alt_path}")
                        return True
                    else:
                        print("Nenhum arquivo CSV encontrado no diretório.")

                except Exception as dir_error:
                    print(f"Erro ao listar diretório: {dir_error}")

        except Exception as head_error:
            print(f"Erro ao verificar existência do arquivo: {head_error}")

        return False