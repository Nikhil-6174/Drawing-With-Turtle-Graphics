from turtle import Turtle, Screen



tim = Turtle()
tim.color("Green")
tim.pencolor("Blue")
tim.shape("circle")
tim.pensize(6)

def move_fw():
    tim.fd(20)

def move_bk():
    tim.bk(20)

def turn_rt():
    tim.rt(25)

def turn_lt():
    tim.lt(25)

def clear():
    tim.home()
    tim.clear()

screen = Screen()
screen.listen()
screen.onkeypress(fun=move_fw,key='W')
screen.onkeypress(fun=move_bk,key='S')
screen.onkeypress(fun=turn_lt,key='A')
screen.onkeypress(fun=turn_rt,key='D')
screen.onkeypress(fun=clear,key='C')

# use capital keys to draw.

screen.title("Welcome to etch a drawing!")
screen.bgcolor('Black')
screen.exitonclick()

