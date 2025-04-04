from unidecode import unidecode


def normalize_text(text):
    """
    Normaliza o texto para busca removendo acentos,
    convertendo para minúsculo e eliminando espaços extras
    """
    if text is None:
        return ""

    # Converter para string caso não seja
    text = str(text)

    # Remover acentos, converter para minúsculo e remover espaços extras
    return unidecode(text.lower().strip())


def calculate_relevance(field_name, text, search_term):
    """
    Calcula a relevância do resultado baseado em onde o termo foi encontrado
    e quão próximo o match é

    Args:
        field_name: Nome do campo onde o termo foi encontrado
        text: Texto onde o termo foi encontrado
        search_term: Termo de busca normalizado

    Returns:
        Pontuação de relevância
    """
    normalized_text = normalize_text(text)

    # Definir pesos por campo
    if field_name in ('razao_social', 'nome_fantasia'):
        base_weight = 5
    elif field_name == 'registro_ans':
        base_weight = 4
    elif field_name == 'cnpj':
        base_weight = 3
    else:
        base_weight = 2

    # Correspondência exata tem peso maior
    if normalized_text == search_term:
        return base_weight * 3

    # Correspondência no início da string tem peso maior
    if normalized_text.startswith(search_term):
        return base_weight * 2

    # Correspondência parcial
    return base_weight