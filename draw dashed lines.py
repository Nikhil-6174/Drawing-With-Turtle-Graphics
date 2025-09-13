from turtle import Turtle, Screen


tom = Turtle()
tom.shape('turtle')
tom.color('Green')
for turns in range(20):
    tom.down()
    tom.fd(10)
    tom.up()
    tom.fd(10)


screen = Screen()
screen.exitonclick()