
import turtle
import time
import random

delay = 0.1

# scores
score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

# Snake_food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.shapesize(.75, .75)
food.penup()
food.goto(.50, .50)


# Pen
pen = turtle.Turtle()
pen.shape("square")
pen.speed(0)
pen.color("forest green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

pen.write(" Score - 0 High Score - {}".format(score, high_score), align="center", font=('Courier', 22, 'normal'))

# Snake_body
segments = []

# Move Functions (directions...)
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def move_up():
    if head.direction!="down":
        head.direction="up"

def move_down():
    if head.direction!="up":
        head.direction="down"

def move_right():
    if head.direction!="left":
        head.direction="right"

def move_left():
    if head.direction!="right":
        head.direction="left"

# keyboard input
wn.listen()
wn.onkeypress(move_up, 'i')
wn.onkeypress(move_down, 'k')
wn.onkeypress(move_right, 'l')
wn.onkeypress(move_left, 'j')

# colors
colors = ['red', 'yellow', 'pink', 'purple', 'blue', 'hot pink']

# MAin game loop
while True:
    wn.update()
    if head.distance(food)<15:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.color(random.choice(colors))
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)

        score = score + 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(" Score - {} High Score - {}".format(score, high_score), align="center", font=('Courier', 22, 'normal'))


    for i in range(len(segments)-1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()

        segments[i].goto(x, y)

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments = []

        score = 0
        pen.clear()
        pen.write(" Score - {} High Score - {}".format(score, high_score), align="center",
                  font=('Courier', 22, 'normal'))

    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments = []
    time.sleep(delay)


wn.mainloop()