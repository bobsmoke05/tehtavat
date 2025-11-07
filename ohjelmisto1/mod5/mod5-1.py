import random

maara = int(input("Noppien määrä: "))

summa = 0

for i in range(maara):
    moi = random.randint(1,6)
    summa += moi

print(summa)
