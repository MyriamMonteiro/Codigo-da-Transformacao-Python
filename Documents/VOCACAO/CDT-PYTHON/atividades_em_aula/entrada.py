##MVC

#model
### def logica_escolha
### while - repete a pergunta
### if - manipula as opções

#view
### def apresentacao
### print(funções()) == console, executar código

#contruller
### input opcao
### input - entrada dos dados
### print - exibe informações

def apresentacao():
    print ("Seja bem-vindo(a) ao Banco MMS!")
    print("-"*20)

    print ("Veja as opções a seguir:\n"
                "1 - Conta Corrente \n"
                "2 - Conta Poupança\n"
                "3 - Encerrar sistema")
    print("-"*20)

def logica_escolha():
#conta_corrente = 1
# conta_poupanca = 2
# encerrar_sistema = 3

    while True:

        #try:
            opcao = int ( input ( "Qual opção deseja acessar? " ) )

            if opcao == 1:
                print ("Você acessou a conta Corrente.")

            elif opcao == 2:
                print ("Você acessou a conta Poupança.")

            elif opcao == 3:
                break
            else:
                print("Opção inválida.")



print(apresentacao())
print(logica_escolha())
