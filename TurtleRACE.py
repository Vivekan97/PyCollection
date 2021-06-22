from turtle import Turtle,Screen
import random
is_game_on = False
screen = Screen()
screen.setup(width=600,height=400)

colours = ["red","blue","green","yellow","orange","purple"]

final = []
y = -100
for i in colours:
    tom = Turtle(shape="turtle")
    tom.color(i)
    tom.penup()
    tom.goto(-280,y)
    y += 50
    final.append(tom)
user = screen.textinput(title="Make your bet",prompt="Pick your Color : ")
print(user)

if user:
    is_game_on = True

while is_game_on:
    for turtle in final:
        if turtle.xcor() > 270:
            is_game_on = False
            if turtle.pencolor() == user:
                print(f"You have Won. The turtle {turtle.pencolor()} is the winner")
            else:
                print(f"You have lost. The turtle {turtle.pencolor()} is the winner")
        dist = random.randint(1,11)
        turtle.forward(dist)


screen.exitonclick()