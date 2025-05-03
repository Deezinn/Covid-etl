import requests
import json
import pandas as pd


class HttpData:
    def __init__(self):
        self.__path = 'urlApis.json'
        self.__urls = []
        self.__header = {
            'Accept': 'application/json'
        }
        self.data = None

    def load_json(self):
        try:
            with open(self.__path, 'r') as file:
                data = json.load(file)
                self.__urls.append(data)
        except FileNotFoundError as e:
            print(f'Erro ao encontrar o arquivo: {e}')
        except FileExistsError as e:
            print(f'Erro de arquivo, verifique o caminho: {e}')
        except ValueError as e:
            print(f'Erro de valor no arquivo, verifique as urls e/ou estrutura do json: {e}')

    def getHttp(self, url):
        try:
            response = requests.get(url, headers=self.__header)
            if response.status_code == 200:
                return response.json()
            else:
                print(f'Erro na requisição de {url}. Status code: {response.status_code}')
                return None
        except requests.exceptions.RequestException as e:
            print(f'Erro ao fazer requisição para {url}: {e}')
            return None

    def insert_http_json(self):
        data = self.__urls[0]
        results = []
        for covid_api in data.get('api_covid', []):
            response_data = self.getHttp(covid_api['url'])
            if response_data:
                results.append(response_data)
        # Aqui fica a escalabilidade, ele lê o json de acordo com a primeira chave e fazemos a extração
        # logo, você deve criar uma classe para tratar esses dados especificamente. (não estou usando.)
        # for world_bank_api in data.get('api_world_bank', []):
        #     response_data = self.getHttp(world_bank_api['url'])
        #     if response_data:
        #         results.append(response_data)
        return results

    def return_data(self):
        self.load_json()
        data = self.insert_http_json()
        return data


