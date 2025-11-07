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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi} - Tilanne:")
        print("-" * 70)
        for auto in self.autot:
            print(auto)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kulj >= self.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    rek = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rek, huippu))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    tunti += 1
    kilpailu.tunti_kuluu()
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

print(f"\nKilpailu päättyi {tunti} tunnin jälkeen!")
kilpailu.tulosta_tilanne()