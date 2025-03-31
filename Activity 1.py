import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle. Turtle()
x = int(input("How many sides does your shape have? "))
side_l = int(input("How long do you want it to be?"))
angle = 360/x
for i in range(x):
    polygon.forward(side_l)
    polygon.right(angle)
turtle.done()