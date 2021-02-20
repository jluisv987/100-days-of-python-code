from turtle import Turtle, Screen
import random
colors = ["red","orange","yellow","green","blue","purple"]
new_turtle = Turtle()
all_turtles=[]
screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")
is_race_on = False
for turtle_i in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y = -70+(turtle_i*30))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0,10)
    for turtle in all_turtles:
        
        if turtle.xcor()>230:
            winning_color= turtle.pencolor()
            if winning_color==user_bet:
                print("You win the bet!!")
            else:
                print(f"You have lost, the winning turtle is {winning_color}")
            is_race_on=False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()