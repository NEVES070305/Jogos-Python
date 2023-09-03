import random


def jogar():

    imprimir_mensagem_abertura()
    letras_acertadas, palavra_secreta = criar_palavra_secreta()

#    for letra in palavra_secreta:
#       letras_acertadas.append("_")
    print(letras_acertadas)
    enforcou = False
    acertou = False
    erro = 0
    possibilidades_de_erros = 6

    while not enforcou and not acertou:
        chute = pedir_chute()
        if(chute in palavra_secreta):
            reescrever_forca_com_acerto(palavra_secreta,letras_acertadas,chute)
        else:
            erro+=1
            if(erro != possibilidades_de_erros):
                print(f"Você ainda têm {possibilidades_de_erros-erro} tentativas.")
            else:
                print("Acabaram-se suas chances.")

        print("Jogando...")
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        #if(erro==6):
        #    enforcou = True
        enforcou = erro == possibilidades_de_erros

    imprimir_mensagem_final(acertou, enforcou)
    

def imprimir_mensagem_abertura():
    print("***********")
    print("**Bem vindo ao jogo da Forca!**")
    print("***********")

def criar_palavra_secreta():
    with open("palavra.txt","r") as arquivo:
        linha_aleatória = random.choice(arquivo.readlines()) #Armazenamento em lista com arquivo.realines()-gerou lista-, e após escolhemos aleaoriamente índice da lista
    

    palavra_secreta = linha_aleatória.strip().upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    return [letras_acertadas, palavra_secreta]

def pedir_chute():
    return input(f"Qual letra?").strip().upper()

def reescrever_forca_com_acerto(palavra_secreta,letras_acertadas,chute):
    index = 0
    for letra in palavra_secreta:
        if(letra == chute):
            letras_acertadas[index] = letra
        index+=1

def imprimir_mensagem_final(acertou, enforcou):
    print("Você ganhou. Fim do jogo" if acertou and not enforcou else "Você se enforcou!")
    
if( __name__ == "__main__"):
    jogar()