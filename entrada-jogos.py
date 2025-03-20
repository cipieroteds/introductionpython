import forca
import jogo_adivinhacao

def escolhe_jogo():
    print("*********************************")
    print(  "Bem vindo ao Salão de Jogos!")
    print("*********************************")

    print("(1) FORCA   (2) ADIVINHAÇÃO")
    jogo = int(input("Escolha o jogo: "))

    if(jogo ==1):
        print("Jogando Forca")
        forca.jogar()   # funcao criada nos outros arquivos para chamar a função
    elif(jogo ==2):
        print("Jogando Adivinhação")
        jogo_adivinhacao.jogar()

if(__name__=="__main__"):   #funcao para que o jogo rode independente do arquivo a ser executado (adivinhacao os entrada)
    escolhe_jogo()
