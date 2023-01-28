import turtle
num_quadrados = 8
tam_quadrados = 40
tam_placa = tam_quadrados * num_quadrados
borda = 1.025
tam_estampa = 20
tela = turtle.Screen()
tela.title("Tabuleiro Jogo de Dama")
tela.setup(450, 450)
tela.tracer(1)
caneta = turtle.Turtle(shape='square', visible=True)
caneta.shapesize(tam_placa / tam_estampa * borda)
caneta.color('black')
caneta.stamp()
caneta.shapesize(tam_quadrados / tam_estampa)
caneta.color('white')
caneta.penup()
for y in range(-num_quadrados // 2, num_quadrados // 2):
    paridade = y % 2 == 0
    for x in range(-num_quadrados // 2, num_quadrados // 2):
        if paridade:
            caneta.goto(x * tam_quadrados + tam_quadrados // 2, y * tam_quadrados + tam_quadrados // 2)
            caneta.stamp()
        paridade = not paridade

caneta.hideturtle()
caneta.up() 
caneta.setpos(-150, -210) 
caneta.down() 
caneta.color('black') 
caneta.write("Thiago Arica", font=("Calibri", 16, "bold"))
       
turtle.done()