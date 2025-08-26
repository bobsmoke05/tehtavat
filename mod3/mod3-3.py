sp = input("Kerro sukupuolesi: ")
hemo = int(input("Anna hemogobliiniarvosi: "))

if sp == "nainen":
    if hemo < 117:
        print("Hemogobliiniarvosi on alhainen")
    elif hemo > 175:
        print("Hemogobliiniarvosi on korkea")
    else:
        print("Hemogobliiniarvosi on normaali")

if sp == "mies":
    if hemo < 134:
        print("Hemogobliiniarvosi on alhainen")
    elif hemo > 195:
        print("Hemogobliiniarvosi on korkea")
    else:
        print("Hemogobliiniarvosi on normaali")