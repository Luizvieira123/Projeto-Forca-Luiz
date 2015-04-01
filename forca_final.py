# Projeto -- Jogo da Forca
#
# Luiz Francisco Modenese Vieira Junior
#


# Funções

def DesenhaForca():
    # desenhando a forca
    import turtle              
    window = turtle.Screen()  
    window.bgcolor("blue")
    window.title("Jogo da Forca")
    tartaruga = turtle.Turtle()
    tartaruga.hideturtle()
    tartaruga.pensize(5)
    tartaruga.penup()
    # base da forca
    tartaruga.setpos(-275,0)
    tartaruga.pendown()
    dist = 50
    angulo1 = 0
    for i in range(1):
        tartaruga.left(angulo1)
        tartaruga.forward(dist)
    tartaruga.penup()       
    # pau vertical para cima
    tartaruga.setpos(-250,0)
    tartaruga.pendown()
    dist = 200
    angulo1 = 90
    for i in range(1):
        tartaruga.left(angulo1)
        tartaruga.forward(dist)
    tartaruga.penup()
    # pau horizontal
    tartaruga.pendown()
    dist2 = 100
    angulo2 = 270
    for i in range(1):
        tartaruga.left(angulo2)
        tartaruga.forward(dist2)
    tartaruga.penup()
    # haste de suporte
    tartaruga.setpos(-250,175)
    tartaruga.pendown()
    tartaruga.left(45)
    tartaruga.forward(35.3)
    tartaruga.penup()
    # pau vertical para baixo
    tartaruga.setpos(-150,200)
    tartaruga.pendown()
    dist3 = 50
    angulo3 = 225 
    for i in range(1):
        tartaruga.left(angulo3)
        tartaruga.forward(dist3)
    tartaruga.penup()

def DesenhaBoneco(parte):
    # desenhando uma parte do boneco
    import turtle
    tartaruga=turtle.Turtle()
    tartaruga.hideturtle()
    tartaruga.penup()
    tartaruga.color("red")
    if parte==0:
        # desenha cabeca
        tartaruga.setpos(-150,110)
        tartaruga.pendown()
        tartaruga.circle(20)
        tartaruga.penup()
    elif parte==1:
        # desenha corpo
        tartaruga.setpos(-150,110)
        tartaruga.pendown()
        tartaruga.left(270)
        tartaruga.forward(70)
        tartaruga.penup()
    elif parte==2:
        # desenha braco direito
        tartaruga.setpos(-150,90)
        tartaruga.pendown()
        tartaruga.left(30)
        tartaruga.forward(50)
        tartaruga.penup()            
    elif parte==3:
        # desenha braco esquerdo
        tartaruga.setpos(-150,90)
        tartaruga.pendown()
        tartaruga.left(150)
        tartaruga.forward(50)
        tartaruga.penup()
    elif parte==4:
        # desenha perna direita
        tartaruga.setpos(-150,50)
        tartaruga.pendown()
        tartaruga.left(300)
        tartaruga.forward(50)
        tartaruga.penup()
    elif parte==5:
        # desenha perna esquerda
        tartaruga.setpos(-150,50)
        tartaruga.pendown()
        tartaruga.left(230)
        tartaruga.forward(50)
        tartaruga.penup()

def LetrasDigitadas(digitadas):
    # Escrevento Letras Digitadas  
    import turtle
    tartaruga=turtle.Turtle()
    tartaruga.hideturtle()
    tartaruga.penup()
    tartaruga.setpos(-100,200)
    tartaruga.write("Letras Digitadas", align="left", font=("Arial", 12, "normal"))
    tartaruga.penup()
    phrz = -100     
    for i in range(len(digitadas)):
        tartaruga.setpos(phrz,180)
        tartaruga.write(digitadas[i], align="left", font=("Arial", 12, "normal"))
        phrz += 20

def LetrasAcertadas(senha):
    #Escrevendo Letras Acertadas
    import turtle
    tartaruga=turtle.Turtle()
    tartaruga.hideturtle()
    tartaruga.hideturtle()
    tartaruga.penup()
    phrz=-100
    size_senha=len(senha)
    for i in range(size_senha):
        if palavra[i] != " ":        
            tartaruga.setpos(phrz,0)
            tartaruga.pendown()
            tartaruga.forward(20)
        tartaruga.penup()
        tartaruga.setpos(phrz,0)
        tartaruga.write(senha[i], align="left", font=("Arial", 20, "normal"))
        phrz=phrz+30

def VerificaCaracteresEspeciais (palavra, tentativa, acertos):
    # verificando caracteres especiais e acentos
    A = ["Ã", "Á", "À", "Â"]
    E = ["É", "È", "Ê"]
    I = ["Í", "Ì", "Î"]
    O = ["Ó", "Ò", "Ô", "Õ"]
    U = ["Ú", "Ù", "Û"]
    C = ["Ç"]
    if tentativa == "A":
        for i in range(0,len(A)-1):
            if A[i] in palavra:
                acertos += A[i]
    if tentativa == "E":
        for i in range(0,len(E)-1):
            if E[i] in palavra:
                acertos += E[i]
    if tentativa == "I":
        for i in range(0,len(I)-1):
            if I[i] in palavra:
                acertos += I[i]
    if tentativa == "O":
        for i in range(0,len(O)-1):
            if O[i] in palavra:
                acertos += O[i]
    if tentativa == "U":
        for i in range(0,len(U)-1):
            if U[i] in palavra:
                acertos += U[i]
    if tentativa == "C":
        for i in range(0,len(C)-1):
            if C[i] in palavra:
                acertos += C[i]

# Programa Principal

import turtle
tartaruga=turtle.Turtle()
tartaruga.hideturtle()
import random

# leitura do Arquivo de Palavras e tamanho de palavras
texto= open("entrada.txt", "r+", encoding ="utf-8")
contador=0
lista_palavras=[]
size_palavras=[]
for linha in texto.readlines():
    if linha != "\n":
        lista_palavras.append(linha.strip())
        lista_palavras[contador]=lista_palavras[contador].upper()
        size_palavras.append(len(lista_palavras[contador]))
        contador += 1
palavra = lista_palavras[random.randint(0,len(lista_palavras)-1)]    
texto.close()

# Programa Principal

digitadas=[]
erros=0
acertos=[]

DesenhaForca()
while True:
    senha=""
    for letra in palavra:
        if letra in acertos:
            senha += letra
        else:
           senha += " "
    LetrasAcertadas(senha)
    if senha == palavra:
        tartaruga.penup()
        tartaruga.setpos(-100,100)
        tartaruga.write("Você Acertou antes de ser Enforcado", align="left", font=("Arial", 15, "bold"))
        break
    tentativa=turtle.textinput("Jogo da Forca", "Digite uma Letra: ").upper().strip()
    if tentativa in digitadas:
        continue
    else:
        digitadas += tentativa
        LetrasDigitadas(digitadas)
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
        VerificaCaracteresEspeciais(palavra, tentativa, acertos)
    if erros == 1:
        DesenhaBoneco(erros-1)
    if erros == 2:
        DesenhaBoneco(erros-1)
    if erros == 3:
        DesenhaBoneco(erros-1)
    if erros == 4:
        DesenhaBoneco(erros-1)
    if erros == 5:
        DesenhaBoneco(erros-1)
    if erros == 6:
        DesenhaBoneco(erros-1)
        tartaruga.penup()
        tartaruga.setpos(-100,100)
        tartaruga.write("Você foi Enforcado antes de Acertar", align="left", font=("Arial", 15, "bold"))
        break

tartaruga.exitonclick()

    
    