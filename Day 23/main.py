import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score_board = Scoreboard()
car_manager = CarManager()
game_is_on = True

player = Player()
screen.listen()
screen.onkey(player.move, "Up")
while game_is_on:
    score_board.update_scoreboard()
    #random car generation
    chance = random.randint(1,6)
    if chance == 1:
        car_manager.create_car()
    car_manager.move_cars()
    #detect collisions
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            score_board.game_over()
            game_is_on=False
    if player.ycor()>270:
        score_board.increase_level()
        player.reset_position()
        car_manager.level_up()
    time.sleep(0.1)

    screen.update()

screen.exitonclick()