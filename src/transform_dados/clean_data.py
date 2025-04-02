def clean_data(df):
    """
    Limpa dados para remover valores nulos ou vazios.
    """
    # Remove completamente linhas vazias
    df = df.dropna(how='all')

    # Substitui valores None por strings vazias
    df = df.fillna('')

    # Remove espaços extras
    for column in df.columns:
        if df[column].dtype == object:
            df[column] = df[column].astype(str).str.strip()

    return df
