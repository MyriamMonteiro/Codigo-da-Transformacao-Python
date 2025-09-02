### Criar funções

#saudações
def saudacao():
    nome = input("Escreva seu nome: ")
    print (f"\nSeja bem vindo(a), {nome}! Confira sua nota final")

def calcular_media():
    nota_1 = float(input("Digite sua primeira nota de 1 a 10: "))
    nota_2 = float(input("Digite sua segunda nota de 1 a 10: "))
    nota_3 = float(input("Digite sua terceira nota de 1 a 10: "))

    soma_media = (nota_1 + nota_2 + nota_3) / 3

    if soma_media >= 7 and soma_media <= 10:
        print(f"Parabéns. Você foi aprovado! Sua nota final foi {soma_media:.2f}")
    else:
        print(f"Infelizmente você foi reprovado.  Sua nota final foi {soma_media:.2f}")

    return [nota_1, nota_2, nota_3]

def maior_menor(notas):
    print ( "\nPara descobrir sua maior e sua menor nota: " )

    maior = max ( notas )
    menor = min ( notas )

    print ( f"A maior nota foi: {maior}" )
    print ( f"A menor nota foi: {menor}" )



saudacao ()
notas = calcular_media()
maior_menor(notas)