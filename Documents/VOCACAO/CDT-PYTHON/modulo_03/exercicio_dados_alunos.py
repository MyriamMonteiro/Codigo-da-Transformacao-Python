#Armazenar informações dos alunos
#nome; idade, notas
#dicionário

lista_alunos = []

def menu():
        print ( "\n Quais operações você quer fazer:" )
        print ( "1 - Cadastrar aluno" )
        print ( "2 - Remover um aluno da lista" )
        print ( "3 - Listar os alunos cadastrados" )
        print ( "4 - Sair" )
        escolha = input("\nEscolha entre 1 a 4: ")
        return escolha

def cadastro():
        al_nome = input("Escreva o nome do aluno(a): ")
        al_idade = int(input("Escreva a idade do aluno(a): "))
        al_nota = float(input("Escreva a nota do aluno(a): "))
        aluno_dicio = {"nome": al_nome, "idade": al_idade, "nota": al_nota }
        lista_alunos.append(aluno_dicio)
        print(f"Você cadastrou o aluno(a) {al_nome} em sua lista")


def remover():
        escolha_remover = input("Digite o nome do aluno a ser removido: ")
        for aluno_dicio in lista_alunos:
                if aluno_dicio["nome"] == escolha_remover:
                        lista_alunos.remove(aluno_dicio)
                        print(f"{escolha_remover} foi removido!")
                        return
                else:
                        print("Aluno não encontrado.")


def listar():
        if lista_alunos :
                print ( "\nVeja a seguir a lista de alunos cadastrados:" )
                for aluno in lista_alunos :
                        print ( f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}" )
        else :
                print ( "\nNenhum aluno cadastrado." )


while True:
    opcao = menu()

    if opcao == "1":
        cadastro()
    elif opcao == "2":
        remover()
    elif opcao == "3":
        listar()
    elif opcao == "4":
        print("Saindo do programa")
        break
    else:
        print("Opção inválida. Tente novamente")

