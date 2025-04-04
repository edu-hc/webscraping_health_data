import os

from api.backend.application import create_app
from api.backend.config import Config

if __name__ == '__main__':
    # Verificar se o arquivo CSV existe antes de iniciar o servidor
    if not os.path.exists(Config.CSV_PATH):
        print(f"ERRO: Arquivo {Config.CSV_PATH} não encontrado!")
        print(f"Certifique-se de que o diretório 'banco_dados/files' existe e contém o arquivo 'Relatorio_cadop.csv'")
    else:
        app = create_app()
        app.run(debug=Config.DEBUG)