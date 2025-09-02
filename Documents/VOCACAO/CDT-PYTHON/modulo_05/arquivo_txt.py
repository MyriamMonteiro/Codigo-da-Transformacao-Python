# Criar um arquivo TXT - modo escrita e leitura
with open("test_arquivo.txt", "w") as arquivo:
    arquivo.write("Essa é uma atividade para criar "
                  "um arquivo txt. através do Python\n")

with open("test_arquivo.txt", "r") as arquivo:
    leitura = arquivo.read()
    print("Aqui é o conteúdo. A parte da leitura do arquivo.txt:")
    print(leitura)



