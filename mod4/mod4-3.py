teksti = input("Luku: ")
pieni = None
suuri = None

while teksti != "":
    luku = int(teksti)
    if pieni is None:
        pieni = luku
        suuri = luku
    else:
        if luku < pieni:
            pieni = luku
        if luku > suuri:
            suuri = luku
    teksti = input("Luku: ")

print(f"Pienin luku: {pieni}. Suurin luku: {suuri}")
