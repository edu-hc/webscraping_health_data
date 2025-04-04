from flask import current_app
import csv

def carregar_dados():
    """Carrega os dados do CSV para memória"""
    dados = []
    with open(current_app.config['CSV_PATH'], mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')
        for linha in reader:
            dados.append(linha)
    return dados