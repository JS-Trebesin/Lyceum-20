import random

seznam_karet = []
seznam_barev = ["♠", "♥", "♦", "♣"]
seznam_hodnot = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

for hodnota in seznam_hodnot:
    for barva in seznam_barev:
        seznam_karet.append(hodnota+barva)   

random.shuffle(seznam_karet)

karty_ruka_hrac = []
karty_ruka_souper = []

def main():
    global seznam_karet, karty_ruka_hrac, karty_ruka_souper
    rozdavej("hrac")
    rozdavej("souper")
    rozdavej("hrac")
    rozdavej("souper")

    print(f"Tvoje karty {karty_ruka_hrac}")

    while True:
        print("Chceš další kartu?")
        akce = input().lower()
        if akce == "a":
            rozdavej("hrac")
            print(f"Tvoje karty {karty_ruka_hrac}")
        elif akce == "n":
            break
        else:
            print("Zadej A nebo N")


    AI(karty_ruka_souper)

    print(f"Tvoje karty {karty_ruka_hrac}")
    spocitana_hodnota_hrac = spocitej_hodnotu_ruky(karty_ruka_hrac)
    print(spocitana_hodnota_hrac)


    print(f"Karty souper {karty_ruka_souper}")
    spocitana_hodnota_souper = spocitej_hodnotu_ruky(karty_ruka_souper)
    print(spocitana_hodnota_souper)

    vitez = zjisti_viteze()
    print(f"Vyhrál {vitez}")

def AI(ruka):
    global seznam_karet, karty_ruka_souper
    hodnota_ruky = spocitej_hodnotu_ruky(ruka)
    while hodnota_ruky < 13:
        rozdavej("souper")
        hodnota_ruky = spocitej_hodnotu_ruky(ruka)


def zjisti_viteze():
    global karty_ruka_hrac, karty_ruka_souper
    spocitana_hodnota_hrac = spocitej_hodnotu_ruky(karty_ruka_hrac)
    spocitana_hodnota_souper = spocitej_hodnotu_ruky(karty_ruka_souper)

    if spocitana_hodnota_hrac > 21:
        return "Soupeř"
    if spocitana_hodnota_souper > 21:
        return "Hráč"
    

    if spocitana_hodnota_souper >= spocitana_hodnota_hrac:
        return "Soupeř"
    else:
        return "Hráč"

def rozdavej(komu):
    global seznam_karet, karty_ruka_hrac, karty_ruka_souper
    karta = seznam_karet.pop(0)
    if komu == "hrac":
        karty_ruka_hrac.append(karta)
    elif komu == "souper":
       karty_ruka_souper.append(karta)

def spocitej_hodnotu_ruky(ruka):
    celkova_hodnota = 0
    for hodnota in ruka:
        if hodnota[0] in ["1", "J", "Q", "K"]:
            celkova_hodnota += 10
        elif hodnota[0] == "A":
            celkova_hodnota += 11
        else:
            celkova_hodnota += int(hodnota[0])
    return celkova_hodnota

if __name__ == "__main__":
    main()


