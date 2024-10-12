import math
import turtle 
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
phi = 137.508 * (math.pi/180.0)

for i in range (20):
    r= 4*math.sqrt(i)
    theta = i*phi
    x=r*math.cos(theta)
    y=r*math.sin(theta)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(150,70)
    turtle.left(110)
    turtle.circle(150,70)
    turtle.end_fill()

turtle.fillcolor("OrangeRed4")
for i in range (80):
    r= 4*math.sqrt(i)
    theta = i*phi
    x=r*math.cos(theta)
    y=r*math.sin(theta)
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(i*137.508)
    turtle.pendown()
    turtle.stamp()
    if(i>50):
        turtle.fillcolor("DarkOrange4")
turtle.end_fill()

turtle.penup()
turtle.goto(0, 200)
turtle.color("white")
turtle.write("Pa que mires que yo sí sé querer bonito", align="center", font={"Arial",25,"bold"})

turtle.hideturtle()

turtle.done()