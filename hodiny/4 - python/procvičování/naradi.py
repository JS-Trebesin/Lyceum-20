# Napište funkci total_price(tools), 
# která pro zadaný seznam tools spočítá celkovou cenu nářadí podle připraveného ceníku. 
# Pokud se na seznamu vyskytuje nástroj, jehož cena není známa, místo celkové ceny se vypíše „Nelze nakoupit“.


price = {
    "luk": 5, 
    "srp": 3, 
    "kosa": 8, 
    "kladivo": 4, 
    "cep": 2, 
    "pila": 6,
}

def total_price(tools):
    
    print("Celkem", 0)
