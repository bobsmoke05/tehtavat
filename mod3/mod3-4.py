vuosi = int(input("Anna vuosiluku: "))

if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("Kyllä on")
    else:
        print("Kyllä on")
else:
    print("Ei ole")