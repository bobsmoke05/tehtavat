def poista_parittomat(luku_lista):
    tulos = []
    for luku in luku_lista:
        if luku % 2 == 0:
            tulos.append(luku)
    return tulos

alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = poista_parittomat(alkuperainen)

print(f"Alkuperäinen lista: {alkuperainen}")
print(f"Karsittu lista: {karsittu}")