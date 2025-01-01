import turtle
bob=turtle.Turtle()
bob.color('red','gold')
bob.begin_fill()
for _ in range(10):
    bob.forward(200)
    bob.left(200)
bob.end_fill()
turtle.done()