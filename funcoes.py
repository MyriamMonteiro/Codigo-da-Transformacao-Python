### Criar funções

#saudações
def saudacao():
    nome = input("Escreva seu nome: ")
    print (f"Seja bem vindo(a), {nome}! Confira sua nota final")

#saudacao()

def calcular_media():
    media_1 = float(input("Digite sua primeira nota de 1 a 10: "))
    media_2 = float(input("Digite sua segunda nota de 1 a 10: "))
    media_3 = float(input("Digite sua terceira nota de 1 a 10: "))

    soma_media = (media_1 + media_2 + media_3) / 3

    if soma_media >= 7 and soma_media <= 10:
        print(f"Parabéns. Você foi aprovado! Sua nota final foi {soma_media:.2f}")
    else:
        print(f"Infelizmente você foi reprovado.  Sua nota final foi {soma_media:.2f}")

#calcular_media()

def maior_menor():
    calcular_media(media_1, media_2, media_3)
    notas = ["media_1, media_2 ,media_3]
    #escreva_notas = float(input("Escreva suas notas separadas em virgulas(,): ")), notas.split(",")

maior_menor()


    media_1 = float(input("Digite sua primeira nota de 1 a 10: "))
    media_2 = float(input("Digite sua segunda nota de 1 a 10: "))
    media_3 = float(input("Digite sua terceira nota de 1 a 10: "))

    if media_1 > media_2 and media_3:
        print(f"{media_1} é a sua maior média.")
    elif media_2 > media_1 and media_3:
        print(f"{media_2} é a sua maior média.")
    elif media_3 > media_2 and media_1:
        print(f"{media_1} é a sua maior média.")
    else:
        print(f)