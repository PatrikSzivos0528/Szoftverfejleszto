def kamatos_kamat(c, r, m, t):
    fv = c * (1 + r/m)**(m*t)
    return fv 

befektetettosszeg = float(input("Mekkora összeget kíván befektetni?"))
vegosszeg = kamatos_kamat(befektetettosszeg, 0.08, 12, 5)
print("A futamido vegen onnek ennyi penze lesz: ", vegosszeg)