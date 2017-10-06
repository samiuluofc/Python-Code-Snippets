import turtle

w = 800
h = 600
turtle.setup(w,h)
turtle.width(10)
turtle.speed(1)
turtle.bgcolor("cyan")
turtle.pencolor("purple4")
turtle.fillcolor("yellow")

turtle.penup()
turtle.goto(200,150)
turtle.setheading(90)
turtle.pendown()

turtle.begin_fill()
turtle.circle(50,180)
turtle.end_fill()

turtle.forward(400)
turtle.write("Samiul",font=("Arial", 20, "bold"))
