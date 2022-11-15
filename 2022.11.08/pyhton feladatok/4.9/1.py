import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()

a = turtle.Screen()
a.bgcolor("pink")
teknos.color("blue")

teknos.speed(20)

for i in range(5):
    teknos.forward(20)
    teknos.left(90)
    teknos.forward(20)
    teknos.left(90)
    teknos.forward(20)
    teknos.left(90)
    teknos.forward(20)
    teknos.left(90)
    teknos.forward(20)

    teknos.penup()
    teknos.forward(20)
    teknos.pendown()


screen.mainloop()