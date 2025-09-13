from turtle import Turtle, Screen


tom = Turtle()
tom.shape('turtle')
tom.color('Green')
for turns in range(4):
    tom.fd(300)
    tom.rt(90)


screen = Screen()
screen.exitonclick()