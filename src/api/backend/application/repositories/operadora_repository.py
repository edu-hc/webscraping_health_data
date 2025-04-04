import pandas as pd
from api.backend.application.models.operadora import Operadora
from api.backend.application.utils.text_utils import normalize_text
from config import Config


class OperadoraRepository:
    """
    Repositório para acesso aos dados de operadoras
    """

    def __init__(self, csv_path=None):
        self.csv_path = csv_path or Config.CSV_PATH
        self._dataframe = None

    def _load_data(self):
        """Carrega os dados do CSV para um DataFrame"""
        try:
            # Carregar CSV assumindo separador de ponto e vírgula
            df = pd.read_csv(self.csv_path, sep=';', encoding='latin1')

            # Normalizar nomes das colunas
            df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

            return df
        except Exception as e:
            print(f"Erro ao carregar o arquivo CSV: {e}")
            return None

    @property
    def dataframe(self):
        """Lazy loading do DataFrame"""
        if self._dataframe is None:
            self._dataframe = self._load_data()
        return self._dataframe

    def find_all(self):
        """Retorna todas as operadoras"""
        if self.dataframe is None:
            return []

        return [Operadora.from_dict(row) for _, row in self.dataframe.iterrows()]

    def find_by_id(self, registro_ans):
        """Busca uma operadora pelo registro ANS"""
        if self.dataframe is None:
            return None

        result = self.dataframe[self.dataframe['registro_ans'] == registro_ans]
        if result.empty:
            return None

        return Operadora.from_dict(result.iloc[0].to_dict())

    def search(self, search_fields):
        """
        Busca operadoras com base em um mapa de campos e termos

        Args:
            search_fields: Dicionário com campos e termos de busca

        Returns:
            Lista de operadoras que correspondem aos critérios
        """
        if self.dataframe is None:
            return []

        # Criar uma cópia do dataframe para não modificar o original
        results = self.dataframe.copy()

        # Aplicar filtros para cada campo
        for field, term in search_fields.items():
            if field in results.columns:
                normalized_term = normalize_text(term)
                results = results[results[field].astype(str).apply(
                    lambda x: normalize_text(x)).str.contains(normalized_term, na=False)]

        # Converter para objetos Operadora
        return [Operadora.from_dict(row) for _, row in results.iterrows()]