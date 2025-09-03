lista = []

while True:
    user_input = input("Moi:")
    if user_input == "":
        break
    else:
        lista.append(int(user_input))

lista.sort(reverse=True)
print(lista[:5])