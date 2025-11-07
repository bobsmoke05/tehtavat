import random

kolme = 0
nelja = 0

moi = ""
hei = ""

while kolme < 3:
    eka = random.randint(0,9)
    moi += str(eka)
    kolme += 1
print(moi)

while nelja < 4:
    toka = random.randint(1,6)
    hei += str(toka)
    nelja += 1
print(hei)


