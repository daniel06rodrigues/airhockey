# -*- coding: utf-8 -*-
"""
Created on Dec 27 2023

@author: Afonso Ferreira, Afonso Leitão, Daniel Rodrigues, Jorge, João Sardeira, Tiago Neutel

Este programa é um jogo de Air Hockey
"""

import turtle #importa a biblioteca do turtle


jogo_hockey = turtle.Screen() #cria a janela de fundo do jogo
jogo_hockey.setup(width = 1280, height = 720) #define o tamanho da janela

#cor do fundo do campo
jogo_hockey.bgcolor("royalblue") 

turtle.penup() #faz com que a caneta não desenhe
turtle.setpos(-600, -320) #canto inferior esquerdo do campo de jogo.

turtle.tracer(0, 0) #desliga a animação do turtle.

#desenha o retângulo do campo de jogo
turtle.pensize(5)
turtle.pencolor("white")
turtle.pendown()
turtle.goto(600, -320)
turtle.goto(600, 320)
turtle.goto(-600, 320)
turtle.goto(-600, -320)

#desenha a linha de meio campo
turtle.penup()
turtle.pensize(3)
turtle.goto(0, -320)
turtle.pendown()
turtle.goto(0, 320)

#desenha o círculo de meio campo
turtle.goto(0, -150)
turtle.circle(150)

#desenha a baliza do lado esquerdo
turtle.penup()
turtle.goto(-600, -140)
turtle.pendown()
turtle.circle(140, extent = 180)
turtle.penup()

turtle.goto(-600, 140)
turtle.right(180)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(20)  # Width
    turtle.left(90)
    turtle.forward(280)  # Height
    turtle.left(90)
turtle.end_fill()



#desenha a baliza do lado direito
turtle.penup()
turtle.goto(600, -140)
turtle.pendown()
turtle.circle(-140, extent = 180)
turtle.penup()

turtle.goto(620, 140)
#turtle.right(180)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for _ in range(2):
    turtle.forward(20)  # Width
    turtle.left(90)
    turtle.forward(280)  # Height
    turtle.left(90)
turtle.end_fill()



turtle.update() #o campo aparece no ecrã



jogo_hockey.mainloop() #mantém a janela aberta