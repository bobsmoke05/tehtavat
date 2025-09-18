moi = {""}

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in moi:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    moi.add(nimi)

for i in moi:
    print(i)