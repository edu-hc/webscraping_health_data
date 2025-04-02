import os
import zipfile


def save_as_csv_and_zip(df, csv_filename, zip_filename):
    """
    Saves the DataFrame as CSV and compresses it into a ZIP file.
    """
    # Salva em CSV
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print(f"CSV file saved as: {csv_filename}")

    # Comprime o CSV em ZIP
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename, os.path.basename(csv_filename))

    print(f"ZIP file created: {zip_filename}")