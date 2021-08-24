import random

print("#################################")
print("Bem vindo ao jogo de advinhação !")
print("#################################")
# definição do número a ser encontrado
numero_secreto = random.randint(1, 100)

# definição do nível de dificuldade
print("Insira o nível de dificuldade")
total_de_tentativas = 0
while (total_de_tentativas < 5):
    dificuldade = int(input("fácil -> (1) médio -> (2) difícil -> (3):"))
    if dificuldade == 1:
        total_de_tentativas = 20
        break
    elif dificuldade == 2:
        total_de_tentativas = 10
    elif dificuldade == 3:
        total_de_tentativas = 5
    else:
        print("Dificuldade inválida, tente novamente")

# definição do corpo do jogo
for rodada in range (0, total_de_tentativas):
    print(f"Rodada {rodada + 1} de {total_de_tentativas} tentativas")
    chute = int(input("Digite um número de 1 a 100: "))
    if(chute < 1 or chute > 100):
        print("Você chutou um número fora do escopo")
        continue
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