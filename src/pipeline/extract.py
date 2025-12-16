import requests

from domain.interfaces import ExtractInterface
from settings.loggin import log

from requests import RequestException

class Extract(ExtractInterface):
    def __init__(self, api_url: dict):
        if not api_url:
            raise ValueError("Não encontrei a url que extrai os dados")

        if not isinstance(api_url, dict):
            raise TypeError("Esperava-se um dict (dicionário)")

        self.__api_url = api_url

    def get_data(self):
        data = {}
        log('info', 'Iniciando processo de extração')
        try:
            for key, api in self.__api_url.items():
                r = requests.get(api, timeout=10)
                if r.status_code == 200:
                    log('info', f"{key}: extraido com sucesso, status: {r.status_code}")
                    data[key] = r.json()
                else:
                    log('error', f"O link: {api} deu erro de status code {r.status_code}. "
                          "Esperava o status code 200")
            log('info', 'Processo de extração finalizada')
            return data
        except RequestException as e:
            log('critical', 'Erro ao extrair os dados, ' \
                  rf'erro: {e}')
            return data
