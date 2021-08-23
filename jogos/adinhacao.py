print("#################################")
print("Bem vindo ao jogo de advinhação !")
print("#################################")

numero_secreto = 76

tentativas = int(input("Insira o número de tentativas: "))
rodada = 1

while (tentativas >= rodada):
    print("Rodada: ", rodada)

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
    rodada += 1

print("############")
print("Fim de jogo!")
print("############")
