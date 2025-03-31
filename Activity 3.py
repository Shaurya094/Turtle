import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("White")
size = 0
while True:
    for i in range(4):
        t.fd(size + 1)
        t.left(90)
        size = size - 5
    size = size +1