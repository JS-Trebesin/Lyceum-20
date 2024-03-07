import csv

def main():
    strikes = {}
    
    nacist_data(strikes)
    akce = input("Pro kontrolu striků zadej K\nPro zápis striků zadej Z\n").lower()

    while True:
        if akce == "k":
            jmeno = zeptej_se_na_input()
            vypis_striky(jmeno, strikes)
            break
        elif akce == "z":
            zapis_strike(strikes)
            uloz_data(strikes)
            break
        else:
            print("Zadej K nebo Z")
            akce = input().lower()

    
    opakovani = input("Pokud chceš zkontrolovat někoho dalšího napiš A\n").lower()
    if opakovani == "a":
        main()
        
def zeptej_se_na_input():
    jmeno = input("Jaké jméno chceš zkontrolovat? ").capitalize()
    return jmeno


def vypis_striky(input_jmeno, strikes):
    if input_jmeno in strikes:
        print(strikes[input_jmeno]) 

def zapis_strike(strikes):
    jmeno = input("Zadej jméno, komu chceš přidat strike? ").capitalize()
    
    if jmeno in strikes:
        strikes[jmeno] += 1
    else:
        strikes[jmeno] = 1
    vypis_striky(jmeno, strikes)

def uloz_data(strikes):
    cesta = "K:\\efkoprogram\\hodiny\\4 - python\\základy\\strikes.csv"
    with open(cesta, "w", newline="") as soubor:

        for jmeno in strikes:
            writer = csv.DictWriter(soubor, delimiter=";", fieldnames=["jmeno", "strikes"])
            writer.writerow({"jmeno": jmeno, "strikes": strikes[jmeno]})

## Alternativní zápis funkce
def alternativni_uloz(strikes):
    with open("K:\\efkoprogram\\hodiny\\4 - python\\základy\\strikes.csv", "w", newline="") as soubor:

        for jmeno in strikes:
            writer = csv.writer(soubor, delimiter=";")
            writer.writerow([jmeno, strikes[jmeno]])

def nacist_data(strikes):
    cesta = "K:\\efkoprogram\\hodiny\\4 - python\\základy\\strikes.csv"
    with open(cesta, "r", newline="") as soubor:
        reader = csv.reader(soubor, delimiter=";")
        for radek in reader:
            strikes[radek[0]] = int(radek[1])

# spusť main pouze pokud se jedná o hlavní program
if __name__ == "__main__":
    main()
