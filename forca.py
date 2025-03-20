import random


def jogar():

    print("*********************************")
    print("Bem vindo ao Jogo de Forca!")
    print("*********************************")

    palavra_secreta = ['banana', 'macarrao', 'brasil', 'fogueira','floresta', 'torneio']
    random.shuffle(palavra_secreta)
    palavra_secreta = (palavra_secreta[0]).upper()
    letras_acertadas = ("_"*len(palavra_secreta))
    print(letras_acertadas)
    letras_corretas = (list(letras_acertadas))
    print(letras_corretas)
    erros = 0

    enforcou = False
    acertou = False

    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()


        print("jogando...")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index = index + 1
        else:
            erros = erros +1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu :(")


    print("Fim de Jogo!")

if(__name__=="__main__"):   #funcao para que o jogo rode independente do arquivo a ser executado (adivinhacao os entrada)
    jogar()