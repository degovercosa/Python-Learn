import forca
import advinhacao

print("#################################")
print("###Bem vindo aos jogos python!###")
print("#################################")
jogo = 0
while jogo < 1 or jogo > 2:
    jogo = int(input("Escolha o seu jogo!! advinhação -> (1), forca -> (2): "))
    if jogo == 1:
        advinhacao.jogar_advinhacao()
    elif jogo == 2:
        forca.jogar_forca()
    else:
        print("Insira um jogo válido")

print("############")
print("Fim do programa!")
print("############")