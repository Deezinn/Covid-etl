from extract.httpData import HttpData


class DataTransform:
    def __init__(self):
        self.httdata = HttpData()
        self.dados = None
        self.traducao_chaves = {
            'updated': 'atualizado_em',
            'country': 'pais',
            'countryInfo': 'info_pais',
            '_id': 'id',
            'iso2': 'sigla2',
            'iso3': 'sigla3',
            'lat': 'latitude',
            'long': 'longitude',
            'flag': 'bandeira',
            'cases': 'casos',
            'todayCases': 'casos_hoje',
            'deaths': 'mortes',
            'todayDeaths': 'mortes_hoje',
            'recovered': 'recuperados',
            'todayRecovered': 'recuperados_hoje',
            'active': 'ativos',
            'critical': 'criticos',
            'casesPerOneMillion': 'casos_por_milhao',
            'deathsPerOneMillion': 'mortes_por_milhao',
            'tests': 'testes',
            'testsPerOneMillion': 'testes_por_milhao',
            'population': 'populacao',
            'continent': 'continente',
            'oneCasePerPeople': 'um_caso_a_cada',
            'oneDeathPerPeople': 'uma_morte_a_cada',
            'oneTestPerPeople': 'um_teste_a_cada',
            'activePerOneMillion': 'ativos_por_milhao',
            'recoveredPerOneMillion': 'recuperados_por_milhao',
            'criticalPerOneMillion': 'criticos_por_milhao'
        }

    def traduzir_chaves(self):
        self.dados = self.httdata.return_data()
        traduzidos = []

        for item in self.dados[0]:
            traduzido = {}
            for chave, valor in item.items():
                nova_chave = self.traducao_chaves.get(chave, chave)

                if isinstance(valor, dict):
                    novo_valor = {}
                    for subchave, subvalor in valor.items():
                        nova_subchave = self.traducao_chaves.get(subchave, subchave)
                        novo_valor[nova_subchave] = subvalor
                    traduzido[nova_chave] = novo_valor
                else:
                    traduzido[nova_chave] = valor

            traduzidos.append(traduzido)
        return traduzidos


