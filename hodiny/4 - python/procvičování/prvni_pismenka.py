def prvni_pismenka(seznam):
    novy_seznam = []
    for slovo in seznam:
        novy_seznam.append(slovo[0])
    return novy_seznam

print(prvni_pismenka(["slon", "zirafa", "krtek"]))