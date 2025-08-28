yritys = 0

while True:
    if yritys == 5:
        print("Pääsy evätty")
        break
    user = input("Käyttäjätunnus: ")
    passw = input("Salasana:")
    if user == "python" and passw == "rules":
        print("Tervetuloa!")
        break
    else:
        yritys += 1