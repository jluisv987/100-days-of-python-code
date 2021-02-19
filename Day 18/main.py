import colorgram
import turtle as turtle_module
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

dots = 100

for dc in range(1,dots+1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)
    if dc %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        
screen = turtle_module.Screen()
screen.exitonclick()
