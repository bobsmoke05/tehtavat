kentat = {"koodi":"nimi"}

while True:
    print("""
    1. Uusi lentoasema
    2. Haku
    3. Lopeta""")
    valinta = int(input())
    if valinta == 3:
        break
    elif valinta == 1:
        koodi = input("ICAO-Koodi: ")
        nimi = input("Nimi: ")
        kentat[koodi] = nimi
    elif valinta == 2:
        koodi = input("ICAO-Koodi: ")
        if koodi in kentat:
            print(f"Lentokenttä {koodi} on {kentat[koodi]}.")
        else:
            print("Ei ole")



