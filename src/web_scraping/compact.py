import os
import zipfile

from src.web_scraping.scraper import download_pdfs


def zip_files(filepaths, zip_name="anexos.zip"):
    """Compacta arquivos em ZIP"""
    try:
        with zipfile.ZipFile(zip_name, "w") as zipf:
            for file in filepaths:
                zipf.write(file, os.path.basename(file))
        print(f"Arquivo {zip_name} criado com sucesso!")
        return zip_name
    except Exception as e:
        print(f"Erro ao compactar: {e}")
        return None
