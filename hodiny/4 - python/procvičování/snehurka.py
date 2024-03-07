cislo = int(input("Zadej číslo"))

for x in range(1, cislo+1):
    if x != 13:
        print(x, end=" ")

    # Alternativní řešní
    if x == 13:
        continue #pass / print(" ", end=" ")
    else:
        print(x, end=" ")

