class Auto:
    def __init__(self, rek, huippu, nyt=0, kulj=0):
        self.rek = rek
        self.huippu = huippu
        self.nyt = nyt
        self.kulj = kulj

    def __str__(self):
        return f"Rekisteritunnus: {self.rek}, huippunopeus: {self.huippu} km/h, nopeus nyt: {self.nyt} km/h, kuljettu matka: {self.kulj} km"


reki = input("Anna rekisterinumero: ")
hui = int(input("Anna huippunopeus (km/h): "))

uus = Auto(reki, hui)

print(uus)
