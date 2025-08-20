### POO - classes, objetos e atributos
#criar Jogo de RPG - Harry Potter

class casas_hp:
    def __init__(self, nome, fundador, caracteristica,) :
        self.nome = nome
        self.fundador = fundador
        self.caracteristica = caracteristica

    def entrar_integrante (self, integrante):
        print(f"{integrante} é um integrante da casa {self.nome}")


sonserina = casas_hp("Sonserina","Salazar Slytherin","ambição")
lufa_lufa = casas_hp("Lufa-Lufa", "Helga Hufflepuff","lealdade")
grifinoria = casas_hp("Grifinória","Godric Gryffindor","coragem")
corvinal = casas_hp("Corvinal","Rowena Corvinal","sabedoria")


### Informações do site que estamos criando (personagens que irão aparecer)
print(f"\nA casa {sonserina.nome} foi fundada por {sonserina.fundador}. E a sua principal caracteristica é a {sonserina.caracteristica}")
print("\n--- Alguns integrantes da Sonserina ---")
sonserina.entrar_integrante("Draco Malfoy")
sonserina.entrar_integrante("Tom Riddle ")
sonserina.entrar_integrante("Regulus Arcturus Black ")

print ( "-" * 20 )

#criar Loja de venda de produtos - Harry Potter

class loja_produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

prod_magicos = []

prod_magicos.append(loja_produto("Mapa do Maroto", 50.99))
prod_magicos.append(loja_produto("Chapéu seletor", 100.60))
prod_magicos.append(loja_produto("Varinha mágica", 25.65))
prod_magicos.append(loja_produto("Uniforme de bruxo", 15.70))

print("--- Loja de Produtos do Harry Potter ---")
for produto in prod_magicos:
    print(f"Produto: {produto.nome} | Preço: R${produto.preco:.2f}")




