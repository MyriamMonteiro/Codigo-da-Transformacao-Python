import random
import math

numero_secreto = random.randint(1, 100)
tentativas = 0

print("🎲 Jogo da Adivinhação! Tente descobrir o número entre 1 e 100.")

while True:
    chute = int(input("Digite seu palpite: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif chute < numero_secreto:
        print("O número é maior.")
    else:
        print("O número é menor.")


print("Dica matemática: a raiz quadrada do número secreto é", round(math.sqrt(numero_secreto), 2))
