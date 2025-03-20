import random

def jogar():

    print("*********************************")
    print("Bem vindo ao Jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)  # type - int funcao round para gerar numero inteiro e random para gerar numero aleatoriao
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000
    #print(numero_secreto)

    print("Nivel de dificuldade:")
    print( "(1) Fácil  (2) Médio (3) Díficil")

    nivel = int(input("Informe o nível: "))

    if(nivel == 1):
        total_de_tentativas = 8
    elif(nivel ==2):
        total_de_tentativas = 6
    else:
        total_de_tentativas = 3

    #Laço com while
    #while(rodada <= total_de_tentativas):
        #print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        #chute_str = input("Digite um número:  ") # type - str
        #print("Você digitou: ", chute_str)
        #chute = int(chute_str) # funcao para converter str em int - para que ao igualar os valores , seja dado como true.

    #Laço com for / range
    for rodada in range(1,total_de_tentativas +1):
        print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
        chute_str = input("Digite um número de 1 a 100:  ") # type - str
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Número inválido, digite novamente.")
            continue

        se_acertou = numero_secreto == chute
        se_chute_maior = chute > numero_secreto
        se_chute_menor = chute < numero_secreto

        if (se_acertou):
            print("Você acertou!Você fez {} pontos!Parabens!" .format(pontos))
            break
        else:
            if(se_chute_maior):
                print("Você errou :(. Seu número é maior que o número secreto.Tente novamente.")
            elif(se_chute_menor):
                print("Você errou :(. Seu número é menor que o número secreto.Tente novamente.")
        pontos_perdidos = abs(numero_secreto - chute) #abs - funcao que retorna somente numero absoluto(retira numero negativo)
        pontos = pontos - pontos_perdidos

    print("Fim de Jogo!")

if(__name__=="__main__"):   #funcao para que o jogo rode independente do arquivo a ser executado (adivinhacao os entrada)
    Jogar()