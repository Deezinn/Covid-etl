BASEURL = 'https://disease.sh/v3/covid-19'

APISURL = {
    'all_cases': f'{BASEURL}/all',
    'states': f'{BASEURL}/states',
    'continents': f'{BASEURL}/continents',
    'countries': f'{BASEURL}/countries'
}

PATHLOG = '../log'

FORMAT = '%(asctime)s %(message)s'
