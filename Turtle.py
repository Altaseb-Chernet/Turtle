import turtle

#setting the screen
screen=turtle.Screen()
screen.bgcolor('black')
screen.title('turtle shapes')

#creating turtle
my_turtle=turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color('white')

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.speed(2)
