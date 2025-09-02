#MVC
#objetivo - lojinha de impressos
# a pessoa pode comprar somente 1 modelo por vez, podendo repetir a quantidade.

#Model
### somar valores dos produtos se tiver mais de 1

#View
### criar menu dos produtos
### print console - resultado da compra

#Contruller
### entrada do usuário na escolha dos produtos
### escolher mais um produto
### finalizar compra

def apresentacao():
    print("Boas vindas a Lojinha de Impressos")

    print(    "Produtos           |  Valores\n"
              "1 - Cartão Postal  |  R$20,00\n"
              "2 - Marca Páginas  |  R$10,00\n"
              "3 - Poster         |  R$30,00\n"
              "4 - Finalizar Compra")


def registro_carrinho():

    while True:
        pergunta = int(input("Escolha um item da lista (digite 1, 2, 3 ou 4): "))

        if (pergunta == 1):
            print("Você adicionou ao carrinho o Cartão Postal")
        elif (pergunta == 2):
            print("Você adicionou ao carrinho o Marca Páginas")
        elif (pergunta == 3):
            print("Você adicionou ao carrinho o Poster")
        elif (pergunta == 4):
            print(f"Obrigada por comprar na Loja de impressos. O total foi de R$")
        else:
            print("Opção inválida. Digite novamente")


def calculo():

    cartao_postal = 20
    marca_pag = 10
    poster = 30

    quantidade = int ( input ( "Qual quantidade deseja comprar? Escolha de 1 a 100: " ) )
    for quantidade in range ()
        quantidade *

print(apresentacao())
print(registro_carrinho())
print(calculo())