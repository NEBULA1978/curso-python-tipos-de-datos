opcion = "z"

while opcion < "a" or opcion > "c":
    print("a Adoro python")
    print("b Detesto python")
    print ("c) Detesto python")

    opcion = input("Opcion: ")

    if opcion == "a":
        print("Me alegro.")
    if opcion == "b":
        print("Que mal.")

    if opcion == "c":
        print("Ya deberias saberlo.")
    else:
        print("Tu opcion  es valida")