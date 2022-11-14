import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")

def sokszog_rajzolas(t, n, h):
    for i in range(n):
        t.forward(n)
        t.left(h)


Eszti = turtle.Turtle()    
sokszog_rajzolas(Eszti, 8, 50)

a.mainloop()

