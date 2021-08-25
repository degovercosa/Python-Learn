

def jogar_forca():
    print("#################################")
    print("Bem vindo ao jogo da forca !")
    print("#################################")
    # definição de variáveis
    palavra_secreta = "macArRao"
    partes_enforcadas = 0
    enforcou = False
    acertou = False
    palavra_encontrada = []

    # dimensão da palavra encontrada
    index1 = 0
    for letra in palavra_secreta:
        palavra_encontrada.insert(index1, "_")

    #game loop
    while( enforcou == False and acertou == False):
        #exibição da palavra encontrada e entrada do chute do usuário
        print(f"Atualmente sua palavra é: {palavra_encontrada}")
        chute = input("Insira uma letra: ")
        chute = chute.strip()

        # comparação da letra chutada com a palavra secreta e inserção da mesma na palavra encontrada
        index2 = 0
        erros = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print(f"Seu chute foi a letra: {chute}")
                print(f"Encontrei a letra {chute} na posição {index2}")
                palavra_encontrada.pop(index2)
                palavra_encontrada.insert(index2, chute)
            else:
                erros +=1
                if (erros == len(palavra_secreta)):
                    print(f"Seu chute foi a letra: {chute}")
                    print("Você chutou a letra errada!!")
                    partes_enforcadas += 1
                    print(f"Você tem {5 - partes_enforcadas} erros restantes")
            index2 += 1

        # verificação da forca
        if (partes_enforcadas > 4):
            print("Infelizmente o número de erros excedeu o limite, você perdeu o jogo da forca :(")
            enforcou = True

        # verificação da vitória
        resultado = "".join(palavra_encontrada)
        if (resultado.upper() == palavra_secreta.upper()):
            print("Parabéns, você acertou a palavra")
            acertou = True

    print("\n")
    print("############")
    print("Fim de jogo!")
    print("############")

if (__name__ == "__main__"):
    jogar_forca()