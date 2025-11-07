pituus = int(input("Kuhan pituus: "))

apituus = 37 - pituus
if pituus < 37:
    print(f"Laske kuha takaisin järveen! Puuttuu {apituus} cm.")
else:
    print("Ota kala")