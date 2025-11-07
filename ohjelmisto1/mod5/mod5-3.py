luku = int(input("Syötä luku: "))

if luku < 2:
    print("Ei alkuluku")
else:
    on_alkuluku = True
    for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print("On alkuluku")
    else:
        print("Ei alkuluku")
