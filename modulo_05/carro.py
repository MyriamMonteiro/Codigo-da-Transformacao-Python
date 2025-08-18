class Carro:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}"

class CarroEletrico(Carro):

    def __init__(self, marca, modelo, autonomia_bateria):

        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        super().exibir_info()
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")

    def __str__(self):
        return f"Carro Elétrico: {self.marca} {self.modelo} ({self.autonomia_bateria} km de autonomia)"

print("--- Testando a classe Carro ---")
carro_a_combustao = Carro("Ford", "Mustang")
carro_a_combustao.exibir_info()
print(carro_a_combustao)
print("-" * 20)

print("\n--- Testando a classe CarroEletrico ---")
carro_eletrico = CarroEletrico("Tesla", "Model S", 652)
carro_eletrico.exibir_info()
print(carro_eletrico)
print("-" * 20)
