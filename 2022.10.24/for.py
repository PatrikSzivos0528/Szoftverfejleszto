a = 1
b = 10

print("Szamolni ",a," tol,",b,"ig")

for x in range (a,b+1):
    print(x)

szo = input("Írd be, hogy kutya! ")
while szo!="kutya":
    print("Nem jó kutya")
    szo = input("Írd be, hogy kutya! ")
print("Ügyes vagy!")