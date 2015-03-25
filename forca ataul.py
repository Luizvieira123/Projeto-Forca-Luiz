
import turtle              
window = turtle.Screen()  
window.bgcolor("blue")
window.title("Jogo da Forca")

tartaruga = turtle.Turtle()
  
# desenhando a forca

tartaruga.pensize(5)
tartaruga.penup()       
tartaruga.setpos(-300,0)
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
    tartaruga.setpos(-200,70)
    tartaruga.color("red")
    tartaruga.pendown()
    tartaruga.circle(40)
cabeca()
    
      
    


window.exitonclick()

    
    