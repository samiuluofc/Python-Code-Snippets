import turtle

n = 10
x = 0

for i in range(n):
    turtle.goto(x,0)
    
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)

    x = x + 30

input()
