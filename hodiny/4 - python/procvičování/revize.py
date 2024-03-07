def dvojnasobek(x,y):
    if x > 2 * y:
        print(x, "je větší než dvojnásobek", y)
    elif x < 2 * y:
        print(x, "není větší než dvojnásobek", y)
    else:
        print(x, "je dvojnásobkem", y)

def delka_slov(seznam):
    novy_seznam = []
    for slovo in seznam:
        novy_seznam.append(len(slovo))
    return novy_seznam

# def delka_slov(seznam):
#     return [len(slovo) for slovo in seznam] 



def countdown(start, n):
    for x in range(start, start-n, -1):
        if x > 0:
            print(x)
        else:
            print("BUM")



countdown(4,7)