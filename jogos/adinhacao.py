print("#################################")
print("Bem vindo ao jogo de advinhação !")
print("#################################")

numero_secreto = 76

chute = int(input("Digite o seu número: "))

print("você digitou: ", chute)

if (numero_secreto == chute):
    print("você acertou")
else:
    print("você errou")