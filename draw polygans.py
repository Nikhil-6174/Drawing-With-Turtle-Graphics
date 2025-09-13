from turtle import Turtle, Screen
from random import choice

tom = Turtle()
tom.shape('turtle')
tom.up()
tom.goto(0,400)
tom.down()
tom.speed(0)
for turns in range(3,10):
    for j in range(turns):
        tom.fd(30)
        tom.rt(360/turns)
        tom.pencolor(choice(['Green','Red','Yellow','Orange','Black','Brown','Grey','Blue','Cyan','Magenta','Pink']))

screen = Screen()
screen.exitonclick()


