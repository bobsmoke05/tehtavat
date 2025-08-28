while True:
    vuosi = int(input("Vuosi: "))
    if vuosi < 1896:
        break
    elif vuosi % 4 == 0 and vuosi != 2020:
        print("Oli olympiavuosi")
    else:
        print("Ei ollut olympiavuosi ")
        if vuosi == 2020:
            print("koska korona, se pidettiin sen sijaan vuonna 2024")
print("Ennen moderneja olympialaisia\nOhjelma lopetettu")