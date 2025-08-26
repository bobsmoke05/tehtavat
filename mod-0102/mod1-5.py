leiviskat = float(input("Anna leiviskät:"))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))

luodin_paino = 13.3
naulan_paino = 32 * luodin_paino
leiviskan_paino = 20 * naulan_paino

paino_grammoina = (leiviskat * leiviskan_paino) + (naulat * naulan_paino) + (luodit * luodin_paino)

kilogrammat = int(paino_grammoina // 1000)
grammat = paino_grammoina % 1000

print("Massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")