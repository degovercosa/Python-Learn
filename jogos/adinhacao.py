print("#################################")
print("Bem vindo ao jogo de advinhação !")
print("#################################")

numero_secreto = 76
total_de_tentativas = int(input("Insira o número de tentativas: "))

for rodada in range (0, total_de_tentativas):
    print("Rodada {} de {} tentativas".format(rodada, total_de_tentativas))
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

print("############")
print("Fim de jogo!")
print("############")
