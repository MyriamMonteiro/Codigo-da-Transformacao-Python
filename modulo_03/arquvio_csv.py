import csv

alunos = [
    ["Nome", "Nota"],
    ["Lucas", 8.7],
    ["Karina", 9.0],
    ["Pedro", 5.2]
]

with open("notas_alunos.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(alunos)

with open("notas_alunos.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    print("\nNotas dos alunos carregadas do arquivo .csv:")
    for linha in leitor:
        print(linha)
