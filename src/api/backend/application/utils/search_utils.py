from fuzzywuzzy import fuzz


def calcular_relevancia(termo, operadora):
    campos = {
        'Razão Social': operadora.get('Razão Social', ''),
        'Nome Fantasia': operadora.get('Nome Fantasia', ''),
        'CNPJ': operadora.get('CNPJ', ''),
        'Registro ANS': operadora.get('Registro ANS', '')
    }

    resultados = []
    for campo, valor in campos.items():
        score = fuzz.partial_ratio(termo.lower(), valor.lower())
        resultados.append({'campo': campo, 'score': score})

    return max(resultados, key=lambda x: x['score'])