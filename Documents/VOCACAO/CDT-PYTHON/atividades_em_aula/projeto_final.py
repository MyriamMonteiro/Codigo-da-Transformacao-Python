#Este projeto é destinado ao trabalho final de conclusão de curso Vocação
#A ideia é desenvolver um catálogo usando Classe, Metodo e atributos. Também será desenvolvida uma organização dos dados, usando JSON.

import json

class cartao_postal:

    def __init__(self, titulo, tema, ano) :

        self.titulo = titulo
        self.tema = tema
        self.ano = ano

    def exibir_info(self) :
        print ("-"*10)
        print (f"Titulo: {self.titulo}")
        print (f"Tema: {self.tema}")
        print (f"Preco: R${self.preco:.2f}")
        print (f"Ano de Criação: {self.ano}")
        print ("-"*10)

def carregar_dados_json(dados_json):
    catalogo = []
    lista_dados = json.loads(dados_json)


