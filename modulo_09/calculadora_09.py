#Para este, vou utilizar o try-except para que o numero não seja divido por zero

def calculadora():

    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        calculo = input("Escolha a operação (+, -, *, /): ")

        if calculo == '+':
            resul = a + b
        elif calculo == '-':
            resul = a - b
        elif calculo == '*':
            resul = a * b
        elif calculo == '/':
            resul = a / b
        else:
            print("Calculo inválido!")
            return

        print(f"O resultado é: {resul}\n")

    except ZeroDivisionError:
        print("Erro: A divisão por zero não é permitida.\n")
    except ValueError:
        print("Erro: O valor digitado não é válido.\n")


calculadora()
