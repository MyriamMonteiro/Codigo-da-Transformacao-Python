import json

clientes = {
    "cliente1": {"nome": "Mirian", "idade": 50},
    "cliente2": {"nome": "Geovana", "idade": 13},
    "cliente3": {"nome": "Myriam", "idade": 25}
}

with open( "../outras_atividades/clientes.json", "w" ) as arquivo_json:
    json.dump(clientes, arquivo_json)

with open( "../outras_atividades/clientes.json", "r" ) as arquivo_json:
    dados = json.load(arquivo_json)

    print("\nClientes carregados do arquivo .json:")
    for cliente, info in dados.items():
        print(f"{cliente}: Nome - {info['nome']}, Idade - {info['idade']}")
