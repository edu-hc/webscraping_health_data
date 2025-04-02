import os
import pandas as pd
import pdfplumber
import re
import zipfile
from tqdm import tqdm  # Biblioteca para mostrar barra de progresso


def extract_tables_from_pdf(pdf_path):
    """
    Extrai todas as tabelas de um PDF contendo o Rol de Procedimentos e Eventos em Saúde.

    Args:
        pdf_path (str): Caminho para o arquivo PDF

    Returns:
        pd.DataFrame: DataFrame combinado contendo todas as tabelas extraídas ou None se nenhuma tabela for encontrada
    """
    print(f"Processando arquivo: {pdf_path}")

    all_tables = []  # Lista para armazenar todas as tabelas encontradas
    table_count = 0  # Contador de tabelas totais

    # Abre o arquivo PDF usando pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"Total de páginas: {total_pages}")

        # Processa cada página do PDF com barra de progresso
        for i, page in enumerate(tqdm(pdf.pages, desc="Extraindo tabelas")):
            # Extrai tabelas da página atual
            try:
                tables = page.extract_tables()

                # Processa cada tabela encontrada na página
                for table in tables:
                    table_count += 1

                    # Verifica se a tabela tem dados (mais de 1 linha)
                    if table and len(table) > 1:
                        # Pega a linha de cabeçalho (primeira linha)
                        header_row = table[0]

                        # Corrige nomes de colunas duplicados se existirem
                        fixed_headers = []
                        header_count = {}

                        # Processa cada cabeçalho de coluna
                        for header in header_row:
                            if header in header_count:
                                header_count[header] += 1
                                fixed_headers.append(f"{header}_{header_count[header]}")
                            else:
                                header_count[header] = 0
                                fixed_headers.append(header)

                        # Converte para DataFrame com cabeçalhos corrigidos
                        df = pd.DataFrame(table[1:], columns=fixed_headers)

                        # Verifica se a tabela contém as colunas esperadas
                        expected_keywords = ['PROCEDIMENTO', 'RN', 'OD', 'AMB']
                        has_columns = any(any(keyword.lower() in str(col).lower()
                                              for keyword in expected_keywords)
                                          for col in df.columns)

                        if has_columns:
                            all_tables.append(df)

            except Exception as e:
                print(f"Erro ao extrair tabelas da página {i + 1}: {e}")

    print(f"Total de tabelas encontradas: {table_count}")
    print(f"Tabelas que atendem aos critérios: {len(all_tables)}")

    # Combina todas as tabelas em um único DataFrame
    if all_tables:
        try:
            # Remove DataFrames vazios
            all_tables = [df for df in all_tables if not df.empty]

            # Corrige colunas duplicadas em cada DataFrame
            for i, df in enumerate(all_tables):
                if df.columns.duplicated().any():
                    print(f"DataFrame {i} tem colunas duplicadas. Corrigindo...")
                    # Renomeia colunas duplicadas adicionando sufixo numérico
                    new_columns = pd.Series(df.columns).astype(str)
                    for idx in df.columns[df.columns.duplicated()].unique():
                        dupe_idxs = df.columns.get_indexer_for([idx] * df.columns.value_counts()[idx])
                        for j, dupe_idx in enumerate(dupe_idxs[1:], 1):
                            new_columns[dupe_idx] = f"{new_columns[dupe_idx]}_{j}"
                    df.columns = new_columns

            # Padroniza nomes de colunas em todos os DataFrames
            all_column_names = set()
            for df in all_tables:
                all_column_names.update(df.columns)

            # Garante que todos os DataFrames tenham as mesmas colunas
            for i, df in enumerate(all_tables):
                for col in all_column_names:
                    if col not in df.columns:
                        all_tables[i][col] = None  # Adiciona coluna faltante com valores None

            # Concatena todos os DataFrames
            combined_df = pd.concat(all_tables, ignore_index=True)
            return combined_df

        except Exception as e:
            print(f"Erro durante concatenação: {e}")

            # Se houver erro, retorna a primeira tabela válida encontrada
            if all_tables:
                print("Retornando a primeira tabela válida em vez de concatenar.")
                return all_tables[0]
            return None
    else:
        print("Nenhuma tabela encontrada que atenda aos critérios.")
        return None