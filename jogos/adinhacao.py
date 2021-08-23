print("#################################")
print("Bem vindo ao jogo de advinhação !")
print("#################################")

numero_secreto = 76
total_de_tentativas = int(input("Insira o número de tentativas de 1 a 20: "))


for rodada in range (0, total_de_tentativas):
    print("Rodada {} de {} tentativas".format(rodada + 1, total_de_tentativas))
    if (total_de_tentativas > 20 or total_de_tentativas < 1):
        print("Você digitou número fora do escopo")
        break
    chute = int(input("Digite um número: "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    print("você digitou: ", chute)

    if (acertou):
        print("você acertou")
        break
    elif (maior):
        print("você errou, seu chute foi maior que o número secreto")
    else:
        print("você errou, seu chute foi menor que o número secreto")

print("############")
print("Fim de jogo!")
print("############")