import random

class Auto:
    def __init__(self, rek, huippu, nyt=0, kulj=0):
        self.rek = rek
        self.huippu = huippu
        self.nyt = nyt
        self.kulj = kulj

    def __str__(self):
        return (f"{self.rek:8} | Huippunopeus: {self.huippu:3} km/h | "
                f"Nopeus nyt: {self.nyt:3} km/h | Kuljettu matka: {self.kulj:6.1f} km")

    def kiihdyta(self, muutos):
        self.nyt += muutos
        if self.nyt > self.huippu:
            self.nyt = self.huippu
        elif self.nyt < 0:
            self.nyt = 0

    def kulje(self, tunnit):
        self.kulj += self.nyt * tunnit


autot = []
for i in range(1, 11):
    rek = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rek, huippu))

kilpailu_kaynnissa = True
tunti = 0

while kilpailu_kaynnissa:
    tunti += 1
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)
        if auto.kulj >= 10000:
            kilpailu_kaynnissa = False
            break

print(f"\nKilpailu päättyi {tunti} tunnin jälkeen!\n")
print("Tulokset:")
print("-" * 70)
for auto in autot:
    print(auto)
