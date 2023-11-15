import forca
import adivinhacao

def escolhe_jogo():
    print("********************")
    print("**Escolha seu jogo**")
    print("********************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? :"))

    if (jogo == 1):
        print("Entrando Jogo da Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Entrando Jogo de Adivinhação")
        Adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()