###menu interativo com while
def menu():
    print ('Opção 1 - Calculadora\n'
            'Opção 2 - "Qual número é o maior?"\n'
            'Opção 3 - classificação das idade')
    print('-'*20)


def mostrar_menu():
    while True:
        try:
            escolha = input ( 'Digite o número 1, 2 ou 3 para as opções acima: ' )
            if escolha == '1':
                calculadora()
            elif escolha == '2':
                num_maior()
            elif escolha == '3':
                idade()
            else:
                print('Opção inválida. Escolha de 1 a 3')
        except ValueError:
            print('Entrada inválida')

###Crie expressões matemáticas - Calculadora
def calculadora():

    print('-'*20)
    print('--CALCULADORA--')
    num1 = float(input('Escreva um número: '))
    num2 = float(input('Escreva outro número: '))
    operador = input ( 'Digite um operador (+, -, /, *) ' )

    resultado = 0

    if operador == '+':
        resultado = num1+num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '/':
        resultado = num1 / num2
    elif operador == '*':
        resultado = num1*num2
    else:
        print('Essa operação não está disponível')

    print('Resultado: ', resultado)

    print('-'*20)

###Qual número é maior?
def num_maior():

    print('-'*20)
    print('Qual número é maior?')
    num1 = int(input('Escreva um número: '))
    num2 = int(input('Escreva outro número: '))

    if num1 > num2:
        print (f'O maior número dos digitados é o {num1}')
    elif num2 > num1:
        print (f'O maior número dos digitados é o {num2}')
    else:
        print('Os números digitados são iguais')

    print('-'*20)


###programa que classifica idade das pessoas
def idade():

    print('-'*20)
    print('Descubra sua categoria - Faixa etária')
    idade = int(input('Digite sua idade em números? '))

    if idade >= 1 and idade <= 12:
        print(f'Tendo {idade} anos, você entra na categoria Criança')
    elif idade >= 13 and idade <= 17:
        print(f'Tendo {idade} anos, você entra na categoria Adolescente')
    elif idade >= 18 and idade <= 59:
        print(f'Tendo {idade} anos, você entra na categoria Adulto')
    elif idade >= 60:
        print ( f'Tendo {idade} anos, você entra na categoria Idoso' )
    else:
        print('Você digitou um número inválido')

(menu())
(mostrar_menu())
(calculadora())
(num_maior())
(idade())