#Lista de compras
from numpy.ma.core import append

print("\n____Faça sua lista de compras para ir ao mercado____\n")

lista = input("Quais produtos deseja comprar? Escreva os produtos separados por virgula: ").split ( ", " )

print ( "\n Edite sua lista: " )
print ( "1 - Adicionar um produto" )
print ( "2 - Remover um produto" )
print ( "3 - Listar os produtos selecionados" )
print ( "4 - Sair" )

while True:

    opcao = input("\nQual opção de 1 a 4 você deseja? ")

    if opcao == "1":
        add_prod = input("Escreva o produto a ser adicionado: ")
        lista.append(add_prod)
        print(f"O Produto {add_prod} foi adicionado com sucesso!")

    elif opcao == "2":
        remove_prod = input("Escreva o produto a ser retirado da lista: ")
        if remove_prod in lista:
            lista.remove(remove_prod)
            print(f"O produto {remove_prod} foi removido da lista")
        else:
            print(f"O produto {remove_prod} já não está na lista")

    elif opcao == "3":
        print(f"Os produtos selecionados são:\n ")
        #para deixar a exibição mais bonita:
        for selecionados in lista:
            print(selecionados)

    elif opcao == "4":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida")
