import turtle

Eszti = turtle.Turtle()

    


def rajzolj_oszlopot(t, magassag):
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.write
    t.write(" "+ str(magassag))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

def diagram(magassag):
      color = ""
      if magassag >= 200:
         color = "red"
      elif magassag < 200 and magassag >= 100:
         color = "yellow"
      elif magassag < 100:
         color = "green"
    
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color()
Eszti.pensize(3)

xs = [48,117,200,240,160,260,220]

for m in xs:
    rajzolj_oszlopot(Eszti, m)
    
ablak.mainloop()