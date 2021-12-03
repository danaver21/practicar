from os import system
import random

print("Bienvenidos a Blackjack")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

continuar=True
b=[]
c=0
g=0
while continuar:
    a=input("Quiere una carta: ")
    mesa=input("Quiere una carta la mesa: ")
    if a=="y":
        posicion=random.randint(0,12)
        b=cards[posicion]
        print(f"user: {b}")
        if b>c or b<c or b==c:
            c+=b
    if c>21:
        d=cards[0]
        d=1

    if mesa=="y":
        posicion=random.randint(0,12)
        f=cards[posicion]
        print(f"mesa: {f}")
        if f>g or f<g or f==g:
            g+=f
    if g>21:
        h=cards[0]
        h=1

    if a=="n" and mesa=="n":
        #continuar=False
        print(c)
        print(g)
        if c>21:
            print("Tu pierdes")
        elif g>21:
            print("mesa pierde")    
        elif c>g:
            print("Tu ganas")
        elif g>c:
            print("mesa gana")
        elif c==g:
            print("mesa gana")        
        c=0
        g=0
        e=input("Quieres volver a jugar 'yes' o 'no': ")
        system("cls")
        if e=="n":
           continuar=False 

        
    

    
