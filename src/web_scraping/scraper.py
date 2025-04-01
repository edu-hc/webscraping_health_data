import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Para lidar com URLs relativas/absolutas

def download_pdfs(url, output_dir="downloads"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9"
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"Erro na requisição: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = []

    # Encontrar todos os links de PDF na página
    for link in soup.select('a[href*=".pdf"]'):  # Alterado para href* (contém .pdf)
        full_url = urljoin(url, link["href"])

        # Filtro mais flexível (ex: captura "Anexo I" ou "Anexo 1")
        if "anexo" in full_url.lower() and "rol" in full_url.lower():
            filename = "Anexo_II.pdf" if "ii" in full_url.lower() else "Anexo_I.pdf"
            pdf_links.append((full_url, filename))

    # Baixar PDFs
    downloaded_files = []
    for pdf_url, filename in pdf_links:
        try:
            pdf_response = requests.get(pdf_url, headers=headers)
            pdf_response.raise_for_status()

            filepath = os.path.join(output_dir, filename)
            with open(filepath, "wb") as f:
                f.write(pdf_response.content)
            downloaded_files.append(filepath)
            print(f"Download realizado: {filename}")
        except Exception as e:
            print(f"Falha ao baixar {pdf_url}: {e}")

    return downloaded_files

