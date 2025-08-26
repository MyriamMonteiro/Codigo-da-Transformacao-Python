class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, Pfisica, saldo=0):
        self.Pfisica = Pfisica
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        print(f"Você sacou: R${valor}. Seu saldo atual: R${self.saldo}\n")

    def depositar(self, valor):
        self.saldo += valor
        print(f"O depósito realizado foi de: R${valor}. Seu saldo atualizado: R${self.saldo}\n")


#saida do codigo:
conta = ContaBancaria("Jonas", 560)
try:
    conta.sacar(1200)
except SaldoInsuficienteError as sie:
    print(f"Erro. O valor ultrapassa o saldo: {sie}")

conta.depositar(156)
