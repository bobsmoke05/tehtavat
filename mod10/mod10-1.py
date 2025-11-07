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


h = Hissi(1, 10)

print("Hissi siirtyy kerrokseen 5:")
h.siirry_kerrokseen(5)

print("Hissi palaa alimpaan kerrokseen:")
h.siirry_kerrokseen(1)