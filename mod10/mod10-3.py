class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros:
            kohdekerros = self.alin_kerros
        elif kohdekerros > self.ylin_kerros:
            kohdekerros = self.ylin_kerros

        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()

        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = []
        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kohdekerros):
        if hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kohdekerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print(f"Hissiä {hissin_numero} ei ole")

    def palohalytys(self):
        print("PALOHÄLYTYS! Kaikki hissit siirtyvät pohjakerrokseen!")
        for i in range(len(self.hissit)):
            print(f"Hissi {i} siirtyy pohjakerrokseen")
            self.hissit[i].siirry_kerrokseen(self.hissit[i].alin_kerros)


talo = Talo(1, 10, 3)

talo.aja_hissia(0, 5)
talo.aja_hissia(1, 8)
talo.aja_hissia(2, 3)

talo.palohalytys()