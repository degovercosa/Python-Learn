print("#################################")
print("Bem vindo ao jogo de advinhação !")
print("#################################")

numero_secreto = 76

tentativas = int(input("Insira o número de tentativas: "))

while (tentativas > 0):

    chute = int(input("Digite o seu número: "))

    acertou = chute == numero_secreto

    maior = chute > numero_secreto

    print("você digitou: ", chute)

    if (acertou):
        print("você acertou")
    elif (maior):
        print("você errou, seu chute foi maior que o número secreto")
    else:
        print("você errou, seu chute foi menor que o número secreto")
    tentativas -= 1
    print("O número de tentativas restantes é: ", tentativas)

print("############")
print("Fim de jogo!")
print("############")
