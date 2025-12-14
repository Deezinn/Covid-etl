import requests

from domain.interfaces import ExtractInterface

class Extract(ExtractInterface):
    def __init__(self, api_url: dict):
        if not api_url:
            raise ValueError("Não encontrei a url que extrai os dados")

        if not isinstance(api_url, dict):
            raise TypeError("Esperava-se um dict (dicionário)")

        self.__api_url = api_url

    def get_data(self):
        data = {}
        try:
            for key, api in self.__api_url.items():
                r = requests.get(api)
                if r.status_code == 200:
                    data[key] = r.json()
                else:
                    print(f"O link: {api} deu erro de status code {r.status_code}. "
                          "Esperava o status code 200")
            return data
        except Exception:
            print('Deu erro na extração')
            return data
