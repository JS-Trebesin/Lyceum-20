import csv

def main():
    strikes = {
        "Katka": 1,
        "Erik": 0,
        "Ondra": 1
        }
    
        
    akce = input("Pro kontrolu striků zadej K\nPro zápis striků zadej Z\n").lower()

    while True:
        if akce == "k":
            jmeno = zeptej_se_na_input()
            vypis_striky(jmeno, strikes)
            break
        elif akce == "z":
            zapis_strike(strikes)
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
    jmeno = input("Zadej jméno, komu chceš přidat strike? ")
    
    if jmeno in strikes:
        strikes[jmeno] += 1
    else:
        strikes[jmeno] = 1
    vypis_striky(jmeno, strikes)

def uloz_data(strikes):
    with open("K:\\efkoprogram\\hodiny\\4 - python\\základy\\strikes.csv", "w", newline="") as soubor:

        for jmeno in strikes:
            writer = csv.DictWriter(soubor, delimiter=";", fieldnames=["jmeno", "strikes"])
            writer.writerow({"jmeno": jmeno, "strikes": strikes[jmeno]})

# spusť main pouze pokud se jedná o hlavní program
if __name__ == "__main__":
    main()
