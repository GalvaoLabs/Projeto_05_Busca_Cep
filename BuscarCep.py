import requests
import json


def buscar_cep(cep_usuario):
    # cep_usuario = input("Informe o seu CEP somente números(sem traços, espaços ou barras):")
    link_api = "https://cep.awesomeapi.com.br/json"
    requisicao_cep = requests.get(f'{link_api}/{cep_usuario}')
    cep_dic = requisicao_cep.json()
    cep = cep_dic.get('cep')
    endereco = cep_dic.get('address')
    bairro = cep_dic.get('district')
    cidade = cep_dic.get('city')
    estado = cep_dic.get('state')
    latitude = float(cep_dic.get('lat'))
    longitude = float(cep_dic.get('lng'))

    return [cep,endereco,bairro,cidade,estado,latitude,longitude]


def descobrir_cep(endereco_usuario):
   link_google = "https://www.google.com/search?q="
   requisicao_google = requests.get(f'{link_google}/{endereco_usuario}')
   return requisicao_google.url
