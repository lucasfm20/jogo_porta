from random import randint
from time import sleep
import textwrap


def linha():
    print("=-"*15)


def espaco():
    print()
    print()

def instrucoes():

    texto="O jogo da porta é um jogo feito para testar sua sorte,ele consiste em você escolher duas portas (a da direita(D) ou a da esquerda (E)),se você escolher a porta destrancada você irá para as próximas duas portas com a mesma funcionalidade, mas se escolher a errada o jogo acaba."
    max=30

    textofinal=textwrap.wrap(texto,max)
    for t in textofinal:
        print(t)

def portaa():
    print(" ________")
    print("|        |")
    print("|    --o |")
    print("|        |")
    print("|        |")
    print("|________|")
    sleep(0.5)

    print(" ________")
    print("|        |")
    print("|      o |")
    print("|     /  |")
    print("|        |")
    print("|________|")
    sleep(0.5)

    print(" ________")
    print("|        |")
    print("|      o |")
    print("|      | |")
    print("|        |")
    print("|________|")
    sleep(0.5)
    
    print("__________")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|        |")
    print("|________|")



def portab():
    print(" ________")
    print("|        |")
    print("|    --o |")
    print("|        |")
    print("|        |")
    print("|________|")
    sleep(0.5)

    print(" ________")
    print("|        |")
    print("|      o |")
    print("|     /  |")
    print("|        |")
    print("|________|")
    sleep(0.5)

    print(" ________")
    print("|        |")
    print("|      o |")
    print("|      | |")
    print("|        |")
    print("|________|")
    sleep(0.5)
    
    print(" ________")
    print("|        |")
    print("|    --o |")
    print("|        |")
    print("|        |")
    print("|________|")



def main():
    c=0
    while True:
        select=randint(1,2) 
        esc= (input("\nEscolha uma porta (D/E):")).strip().upper()[0]
    
        
        while esc not in "DE" :
            print("Erro, digite novamente:")
            esc= (input("\nEscolha uma porta (D/E):")).strip().upper()[0]

        if esc=="D" and select==1:
            portaa()
            print("\nPorta aberta")    
            c+=1
        
        elif esc=="E" and select ==2:
            portaa()
            print("\nPorta aberta")
            c+=1

        else:
            portab()
            print("\nEssa porta estava fechada!!\n")
            break

    cal=(0.5**c)*100

    linha()
    print(f"Você passou por {c} porta(s)")
    if c>0:
        print(f"A probabilidade de abrir essa quantidade de portas é de {cal}%")
    linha()
    espaco()
    


while True:
    sleep(1)
    print()
    linha()
    print("JOGO DAS PORTAS")
    linha()
    print("1-Começar jogo")
    print("2-Sair")
    print("3-Instruções")

    esc=str(input("\nEscolha uma opção:"))

    if esc== "1":
        main()
    
    elif esc== "2":
        print()
        break
    
    elif esc=="3":
        print()
        instrucoes()

    else:
        print("Digite novamente!")


sleep(0.5)
print("Saindo....")
espaco()