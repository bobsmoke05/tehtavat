vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukausi = int(input("Syötä kuukauden numero (1-12): "))

if kuukausi in (12, 1, 2):
    vuodenaika = vuodenajat[0]
elif kuukausi in (3, 4, 5):
    vuodenaika = vuodenajat[1]
elif kuukausi in (6, 7, 8):
    vuodenaika = vuodenajat[2]
else:
    vuodenaika = vuodenajat[3]

print(f"Kuukausi {kuukausi} on vuodenaikaan {vuodenaika}.")