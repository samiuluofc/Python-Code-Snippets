import turtle

sidelen = 50

for i in range(12345678):       # effectively infinite for this purpose
    n = int(input('Enter a positive integer: '))

    turtle.reset()
    for j in range(n):
        turtle.fd(sidelen)
        turtle.lt(360 // n + 180)
        turtle.fd(sidelen)

