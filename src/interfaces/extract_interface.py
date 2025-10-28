from abc import ABC, abstractmethod

class ExtractInterface(ABC):
    """
    Interface para classes responsáveis pela extração de dados.
    """

    @abstractmethod
    def get(self):
        """
        Executa as requisições HTTP para todas as URLs em APISURL e armazena os resultados.
        
        Returns:
            dict: Dicionário contendo os dados de 'all', 'states', 'continents' e 'countries'.
        
        Raises:
            HTTPError: Quando ocorre erro HTTP.
            ConnectionError: Quando há falha de conexão.
            ConnectTimeout: Quando há timeout de conexão.
            URLRequired: Quando a URL está ausente.
            RequestException: Para outros erros de requisição.
        """
        
        pass
