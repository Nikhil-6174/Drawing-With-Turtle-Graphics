import turtle as t
import random


tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')

def rand_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return(r,g,b)

x = 20

for times in range(x+1):
        tim.circle(100)
        tim.left(360/x)
        tim.pencolor(rand_color())


screen = t.Screen ()
screen.exitonclick()
