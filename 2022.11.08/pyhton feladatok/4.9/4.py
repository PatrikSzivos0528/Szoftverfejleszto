import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()

screen.bgcolor("lightgreen")
turtle.color("blue")
# 360 / 20 = 18
for i in range(20):
    turtle.forward(100)
    turtle.forward(-100)
    turtle.left(18)
    
    
turtle.penup()
turtle.left(45)
turtle.forward(147)
turtle.left(140)
turtle.pendown()

for i in range(1):
    for j in range(4):
        turtle.forward(200)
        turtle.left(90)
    
screen.mainloop()


