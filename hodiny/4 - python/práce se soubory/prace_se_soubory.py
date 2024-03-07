import csv


with open("K:\\efkoprogram\\hodiny\\4 - python\\základy\\data.csv", "w") as soubor:

    jmeno = input("Zadej jméno: ")
    pocet_striku = 3

    writer = csv.writer(soubor, delimiter=";")
    writer.writerow([jmeno, pocet_striku])


