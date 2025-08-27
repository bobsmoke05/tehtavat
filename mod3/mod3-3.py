sp = input("Kerro sukupuolesi: ")
hemo = int(input("Anna hemoglobiiniarvosi: "))

if sp == "nainen":
    if hemo < 117:
        print("Hemoglobiiniarvosi on alhainen")
    elif hemo > 175:
        print("Hemoglobiiniarvosi on korkea")
    else:
        print("Hemoglobiiniarvosi on normaali")

if sp == "mies":
    if hemo < 134:
        print("Hemoglobiiniarvosi on alhainen")
    elif hemo > 195:
        print("Hemoglobiiniarvosi on korkea")
    else:
        print("Hemoglobiiniarvosi on normaali")