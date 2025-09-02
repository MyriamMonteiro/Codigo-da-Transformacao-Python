from faker import Faker

gerador = Faker("pt_BR")

numero_de_pessoas = 5

print("--- Gerando Dados de Pessoas ---")
for i in range(numero_de_pessoas):
    nome = gerador.name()
    email = gerador.email()
    endereco = gerador.address()

    
    print(f"\n--- Pessoa {i+1} ---")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Endereço: {endereco}")
    print("-" * 20)

print("\nDados gerados com sucesso!")