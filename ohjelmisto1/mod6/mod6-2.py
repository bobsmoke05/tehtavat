import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Syötä nopan tahkojen määrä: "))

tulos = 0
while tulos != tahkot:
    tulos = heita_noppaa(tahkot)
    print(tulos)

print("Jippii")