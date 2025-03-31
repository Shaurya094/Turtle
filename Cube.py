import turtle
t = turtle.Turtle()
t.speed(10) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

for i in range(4):
  t.forward(100)
  t.right(90)

for i in range(10):
	t.left(45)
	t.forward(10)
	t.right(45)
t.forward(10)

t.forward(100)

for i in range(1):
  t.right(137)
t.forward(110)

t.right(313)
t.forward(99)

for i in range(10):
	t.right(230)
	t.forward(10)
	t.left(230)
t.forward(10)

t.left(180)
t.forward(120)

turtle.done()