from src.interfaces import ExtractInterface
from src.utils import APISURL

import requests
from requests import HTTPError, ConnectionError, ConnectTimeout, URLRequired, RequestException


class Extract(ExtractInterface):
    def __init__(self):
        self.__covid_all = None
        self.__covid_states = None
        self.__covid_continents = None
        self.__covid_countries = None
    
    def get(self):
        try:
            for id_,api in APISURL.items():
                r = requests.get(api, timeout=15)
                if r.status_code == 200:
                   match id_:
                        case 'all':
                           self.__covid_all = r.json()
                        case 'states':
                            self.__covid_states = r.json()
                        case 'continents':
                            self.__covid_continents = r.json()
                        case 'countries':
                            self.__covid_countries = r.json()
                        case _:
                            raise ValueError("Não existe esse id")
        except HTTPError as e:
            raise HTTPError(f"Erro com o método http /n erro: {e}")
        except ConnectionError as e:
            raise ConnectionError(f"Erro de conexão /n erro: {e}")
        except ConnectTimeout as e:
            raise ConnectTimeout(f"Erro de timeout /n erro: {e}")
        except URLRequired as e:
             raise URLRequired(f"Erro, url precisa ser inserida /n erro: {e}")
        except RequestException as e:
            raise RequestException(f"Erro de requisição /n erro: {e}")
        else:
            return {
                'all': self.__covid_all,
                'states': self.__covid_states,
                'continents': self.__covid_continents,
                'countries': self.__covid_countries
            }
