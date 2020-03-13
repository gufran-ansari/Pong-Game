# Simple Pong Game in Python 3

# Step 1: Getting Started

import turtle
import winsound  # To Add Sound
import tkinter as tk
from tkinter import simpledialog

# Window
root = tk.Tk()
root.withdraw()
player = simpledialog.askstring(title="User's Name", prompt="Enter Your Name: ")

win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # will stop screen update automatically

# Step 2: Adding Paddles and Ball
# Paddle
left_paddle = turtle.Turtle()
left_paddle.speed(2)  # Animation speed
left_paddle.shape("square")
left_paddle.color("green")
left_paddle.shapesize(stretch_wid=5, stretch_len=1.5)
left_paddle.penup()
left_paddle.goto(-350, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(2)  # Animation speed
right_paddle.shape("square")
right_paddle.color("yellow")
right_paddle.shapesize(stretch_wid=5, stretch_len=1.5)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Animation speed
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.6  # d means delta/speed
ball.dy = 0.6  # x and y is co-ordinates

# Score
score_a = 0
score_b = 0

# Scoring System
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"{player}: {score_a}  Computer: {score_b}", align="center", font=("Courier", 18, "normal"))


# Step 3: Function
# Paddle Left
def paddle_left_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def paddle_left_down():
    y = left_paddle.ycor()
    y += -20
    left_paddle.sety(y)


# Paddle Right
def paddle_right_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def paddle_right_down():
    y = right_paddle.ycor()
    y += -20
    right_paddle.sety(y)


# Step 4: Keyboard Binding
win.listen()

# Paddle Moving
win.onkeypress(paddle_left_up, "w")  # Moving Up using W Key
win.onkeypress(paddle_left_down, "s")  # Moving Up using S Key

win.onkeypress(paddle_right_up, "Up")  # Moving Up using Up Navigation Key
win.onkeypress(paddle_right_down, "Down")  # Moving Up using Down Navigation Key

# Step 5: Main Game Loop
while True:
    win.update()

    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border
    # Top Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play Sound
        # "winsound.SND_ASYNC" this command will not stop program

    # Bottom Border
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Right Border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write(f"{player}: {score_a}  Computer: {score_b}", align="center", font=("Courier", 18, "normal"))

    # Left Border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write(f"{player}: {score_a}  Computer: {score_b}", align="center", font=("Courier", 18, "normal"))

    # Paddle and Ball Collisions
    # Paddle Right
    if (ball.xcor() > 325 and ball.xcor() < 350) and (
            ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(325)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle Left
    if (ball.xcor() < -325 and ball.xcor() > -350) and (
            ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-325)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
