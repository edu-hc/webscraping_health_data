class Operadora:
    """
    Modelo que representa uma operadora de saúde
    """

    def __init__(self, registro_ans=None, cnpj=None, razao_social=None,
                 nome_fantasia=None, modalidade=None, **kwargs):
        self.registro_ans = registro_ans
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.modalidade = modalidade

        # Atributos adicionais que podem vir do CSV
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        """Converte o objeto para um dicionário"""
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância a partir de um dicionário"""
        return cls(**data)