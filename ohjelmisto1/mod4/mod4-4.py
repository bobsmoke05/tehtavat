import random

numero = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa numero: "))
    if arvaus == numero:
        print("OIKEIN!")
        break
    if arvaus > numero:
        print("Liian suuri arvaus")
    if arvaus < numero:
        print("Liian pieni arvaus")