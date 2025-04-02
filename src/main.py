import traceback

from clean_data import clean_data
from etl.replace_abb import replace_abbreviations
from extract_tables import extract_tables_from_pdf
from save_csv_zip import save_as_csv_and_zip
from web_scraping.compact import zip_files
from web_scraping.scraper import download_pdfs

def main():
    # Configurações
    pdf_path = "downloads/Anexo_I.pdf"
    csv_path = "downloads/Rol_Procedimentos.csv"
    your_name = "Eduardo"
    zip_path = "downloads/Anexo_csv.zip"
    target_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    downloaded = download_pdfs(target_url)

    try:
        if downloaded:
            print("Downloads concluídos com sucesso!")
            zip_files(downloaded, "downloads/anexos.zip")

        else:
            print("Nenhum PDF encontrado.")

    except Exception as e:
        print(f"Erro durante o processamento: {str(e)}")
        traceback.print_exc()


    # Extract tables from PDF
    tables_df = extract_tables_from_pdf(pdf_path)

    if tables_df is not None:
        # Replace abbreviations
        tables_df = replace_abbreviations(tables_df)

        # Clean data
        tables_df = clean_data(tables_df)

        # Save as CSV and compress to ZIP
        save_as_csv_and_zip(tables_df, csv_path, zip_path)
        print("Processing completed successfully!")
    else:
        print("Could not extract tables from the PDF.")


if __name__ == "__main__":
    main()