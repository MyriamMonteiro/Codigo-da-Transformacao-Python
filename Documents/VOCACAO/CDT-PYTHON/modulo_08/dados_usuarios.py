#validar a idade do usuário, garantindo o número positivo.

def dados_usuarios():
    while True :
        try :
            nome = input ("Digite seu primeiro nome: ")

            idade = int (input ("Digite sua idade(em números): "))
            if idade <= 0:
                raise ValueError ("Erro. Não escrever números negativos e 0.")

            print (f"O(a) cliente {nome} com {idade} anos, foi cadastrado no sistema.\n" )
            break

        except ValueError as ve:
            print (f"Erro: {ve}. Tente novamente.\n")


dados_usuarios()
