import pandas as pd

from api.backend.application.repositories.operadora_repository import OperadoraRepository
from api.backend.application.utils.text_utils import normalize_text, calculate_relevance
from config import Config


class OperadoraService:
    """
    Serviço para lógica de negócio relacionada a operadoras
    """

    def __init__(self, repository=None):
        self.repository = repository or OperadoraRepository()

    def search_operadoras(self, search_term, limit):
        """
        Realiza uma busca textual nas operadoras

        Args:
            search_term: Termo a ser buscado
            limit: Limite de resultados

        Returns:
            Lista de operadoras ordenadas por relevância
        """
        # Validar termo de busca
        if not search_term or len(search_term) < Config.MIN_SEARCH_LENGTH:
            return []

        normalized_term = normalize_text(search_term)

        # Campos a serem pesquisados
        search_fields = ['razao_social', 'nome_fantasia', 'registro_ans', 'cnpj', 'modalidade']

        df = self.repository.dataframe
        if df is None:
            return []

        df = df.drop_duplicates()
        results = []

        # Buscar em cada campo
        for field in search_fields:
            if field in df.columns:
                # Filtrar registros que contêm o termo no campo atual
                field_str = df[field].astype(str).apply(normalize_text)
                matches = df[field_str.str.contains(normalized_term, na=False)].copy()

                # Se encontrou correspondências, calcular relevância e adicionar aos resultados
                if not matches.empty:
                    # Adicionar coluna de relevância
                    matches['relevance'] = matches.apply(
                        lambda x: calculate_relevance(field, x[field], normalized_term),
                        axis=1
                    )
                    matches['match_field'] = field
                    results.append(matches)

        # Se não encontrou nada, retornar lista vazia
        if not results:
            return []

        # Concatenar resultados, remover duplicatas e ordenar por relevância
        all_results = pd.concat(results).drop_duplicates(subset=['registro_ans'])
        all_results = all_results.sort_values('relevance', ascending=False)

        # Converter para objetos Operadora
        limited_results = all_results.head(limit)

        # Converter para objetos Operadora
        operadoras = []
        for _, row in limited_results.iterrows():
            # Remover colunas auxiliares antes de criar o objeto
            row_dict = row.to_dict()
            if 'relevance' in row_dict:
                del row_dict['relevance']
            if 'match_field' in row_dict:
                del row_dict['match_field']

            operadoras.append(row_dict)

        return operadoras