def najdi_nejdelsi_slovo(seznam):
    nejdelsi = ""
    for slovo in seznam: 
        if len(slovo) > len(nejdelsi):
            nejdelsi = slovo
    print(nejdelsi)


najdi_nejdelsi_slovo(["slon", "prase", "koza", "pes", "krava"])
