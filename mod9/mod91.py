class Auto:
    def __init__(self, tunnus, huippu, nopeus = 0, matka = 0):
        self.tunnus = tunnus
        self.huippu = huippu
        self.nopeus = nopeus
        self.matka = matka

    def kiihdyta(self, muutos):
        auto.nopeus += muutos
        if auto.nopeus > self.huippu:
            self.nopeus = self.huippu
        elif self.nopeus < 0:
            self.nopeus = 0



auto = Auto("ABC-123", 142)

auto.kiihdyta(20)

auto.kiihdyta(70)

auto.kiihdyta(50)

print(auto.tunnus, auto.huippu, auto.nopeus, auto.matka)

auto.kiihdyta(-200)

print(auto.tunnus, auto.huippu, auto.nopeus, auto.matka)