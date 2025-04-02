def replace_abbreviations(df):
    """
    Substitui abreviações OD e AMB
    """
    od_mapping = {
        'OD': 'Seg. Odontológica',
        'Seg. Odontológica': 'Seg. Odontológica'  #Caso já tenha sido feita substituição
    }

    amb_mapping = {
        'AMB': 'Seg. Ambulatorial',
        'Seg. Ambulatorial': 'Seg. Ambulatorial'  #Caso já tenha sido feita substituição
    }

    # Renomeia colunas se elas já existirem
    if 'OD' in df.columns:
        df = df.rename(columns={'OD': 'Seg. Odontológica'})

    if 'AMB' in df.columns:
        df = df.rename(columns={'AMB': 'Seg. Ambulatorial'})

    return df
