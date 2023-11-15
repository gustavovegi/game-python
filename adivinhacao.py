import random

def jogar():
    print("bem vindo ao jogo de adivinhação")

    numero_secreto= int(random.randrange(1,101))
    tentativas = 0
    pontos = 1000

    print("qual nivel de dificuldade?" )
    nivel= int(input("(1)facil (2)medio (3)dificil"))
    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel ==3:
        tentativas = 3
    else:
        print("erro")

    for rodada in range(1,tentativas + 1):
        print(f"tentativa: {rodada} de {tentativas}")
        chute = int(input("me diga qual seu chute entre 1 e 100"))


        if (chute < 1 or chute > 100):
            print("voce deve digitar um numero entre 1 e 100")
            continue

        acertou =  chute == numero_secreto
        maior = chute > numero_secreto
        menor =  chute < numero_secreto

        if (acertou):
            print(f"voce acertou e fez {pontos} pontos")
            break
        else:
            if (maior):
                print("seu chute foi maior q o numero")
            elif (menor):
                print("seu chute foi menor q  o numero")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print(f"o numero certo era {numero_secreto}")

if (__name__ == "__main__"):
    jogar()