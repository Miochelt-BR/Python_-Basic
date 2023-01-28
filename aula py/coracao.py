import turtle
from turtle import Turtle, Screen

caneta = turtle.Turtle()

tela = Screen()
tela.bgcolor("fuchsia")

def curva(): 
    for i in range(200): 
        caneta.right(1) 
        caneta.forward(1)
        
def coracao():
    caneta.pensize(2)
    caneta.fillcolor('red') 
    caneta.begin_fill() 
    caneta.left(140) 
    caneta.forward(113) 
    curva() 
    caneta.left(120) 
    curva() 
    caneta.forward(112) 
    caneta.end_fill()
    
def texto():
    caneta.up() 
    caneta.setpos(-60, 90) 
    caneta.down() 
    caneta.color('White') 
    caneta.write("Eu Amo minha mulher", font=("Calibri", 16, "bold"))

   
    
coracao() 
texto() 

caneta.hideturtle()
tela.exitonclick()