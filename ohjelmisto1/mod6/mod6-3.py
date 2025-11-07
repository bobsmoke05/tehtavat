def gallonoista_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Syötä bensiinin määrä gallonoina: "))

    if gallonat < 0:
        print("Loppu.")
        break

    litrat = gallonoista_litroiksi(gallonat)
    print(f"{litrat:.2f} litraa")