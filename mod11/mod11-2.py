class Auto:
    def __init__(self, rek, huippu):
        self.rek = rek
        self.huippu = huippu
        self.nyt = 0
        self.kulj = 0

    def kiihdyta(self, muutos):
        self.nyt += muutos
        if self.nyt > self.huippu:
            self.nyt = self.huippu
        elif self.nyt < 0:
            self.nyt = 0

    def kulje(self, tunnit):
        self.kulj += self.nyt * tunnit

class Sähköauto(Auto):
    def __init__(self, rek, huippu, kapasiteetti):
        super().__init__(rek, huippu)
        self.kapasiteetti = kapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rek, huippu, tankki):
        super().__init__(rek, huippu)
        self.tankki = tankki

sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(120)
polttomoottoriauto.kiihdyta(100)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauto {sahkoauto.rek} on ajanut {sahkoauto.kulj} km")
print(f"Polttomoottoriauto {polttomoottoriauto.rek} on ajanut {polttomoottoriauto.kulj} km")