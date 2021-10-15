import turtle

def square(x,a):
    count = 0

    while count < a:
        turtle.fd(x)
        turtle.rt(90)
        turtle.fd(x)
        turtle.rt(90)
        turtle.fd(x)
        turtle.rt(90)
        turtle.fd(x)
        turtle.rt(95)
        count = count + 1

square(100, 30)