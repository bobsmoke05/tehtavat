import random

def noppa(suuruus):
    moi = random.randint(1, suuruus)
    return(moi)

hei = int(input("Kuinka isoa noppaa heitetään"))
print("Nopasta tuli ", noppa(hei))

