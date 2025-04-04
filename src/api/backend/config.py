import os
from pathlib import Path


# Configurações da aplicação
class Config:
    # Diretório base é o diretório atual
    BASE_DIR = Path(__file__).resolve().parent.parent.parent  # sobe 3 níveis

    # Caminho para o arquivo CSV
    CSV_PATH = f'{BASE_DIR}/banco_dados/files/Relatorio_cadop.csv'

    # Configurações da API
    DEBUG = True
    MIN_SEARCH_LENGTH = 3