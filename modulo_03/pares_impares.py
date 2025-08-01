#Programa que descubra se o número é par ou impar
#criar loop

while True:
    num = int ( input ( "Digite um número e descubra se é par ou ímpar: " ) )

    if num % 2 == 0:
        print(f"O número {num} é um número par!")
    else:
        print(f"O número {num} é ímpar!")