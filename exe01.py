import json

import requests

URL = 'https://restcountries.com/v3.1/all'

def requisicao(url):
    try:
        resposta = requests.get(URL) #requisição
        if resposta.status_code == 200:
            return resposta.text

    except:
        print('erro ao fazer requisição', url)

def converter(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta) #a resposta da requisição é convertida em objeto do python
    except:
        print('erro ao fazer a parsing')

def mostrar_populacao(nome_do_pais):
    pass

def contagem_de_paises(lista_de_paises):
    return len(lista_de_paises)

