
import turtle              
window = turtle.Screen()  
window.bgcolor("blue")
window.title("Jogo da Forca")

tartaruga = turtle.Turtle()
  
# desenhando a forca

tartaruga.pensize(5)
tartaruga.penup()       
tartaruga.setpos(-250,0)
tartaruga.pendown()

dist = 200
angulo1 = 90
 
for i in range(1):
   tartaruga.left(angulo1)
   tartaruga.forward(dist) 

dist2 = 100
angulo2 = 270
 
for i in range(1):
   tartaruga.left(angulo2)
   tartaruga.forward(dist2)

dist3 = 50
angulo3 = 270 

for i in range(1):
  tartaruga.left(angulo3)
  tartaruga.forward(dist3)

#desenhando o boneco
def cabeca ():
    import turtle
    tartaruga=turtle.Turtle()
    tartaruga.penup()
    tartaruga.setpos(-150,110)
    tartaruga.color("red")
    tartaruga.pendown()
    tartaruga.circle(20)
cabeca()
    
def corpo ():
    import turtle
    tartaruga=turtle.Turtle()
    tartaruga.penup()
    tartaruga.setpos(-150,110)
    tartaruga.pendown()
    tartaruga.color("red")
    tartaruga.left(270)
    tartaruga.forward(70)
    
corpo()

def bracodireito():
    import turtle
    tartaruga=turtle.Turtle()
    tartaruga.color("red")
    tartaruga.penup()
    tartaruga.setpos(-150,90)
    tartaruga.pendown()
    tartaruga.left(30)
    tartaruga.forward(50)
    tartaruga.color("red")
    
bracodireito()

def bracoesquerdo():
    import turtle
    tartaruga=turtle.Turtle()
    tartaruga.color("red")
    tartaruga.penup()
    tartaruga.setpos(-150,90)
    tartaruga.pendown()
    tartaruga.left(150)
    tartaruga.forward(50)
bracoesquerdo()
    
window.exitonclick()

    
    