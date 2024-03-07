# Napište funkci size_info(n, k), která vypíše pro všechna 
# čísla od 1 do n velmi užitečnou informaci o tom, zda je menší, rovno, nebo větší než k.


def size_info(n, k):
    for x in range(1, n+1):
        if x > k:
            print(x, "větší než", k)
        elif x == k:
            print(x, "je stejné jak", k)
        else: 
            print(x, "menší než", k)

size_info(10, 4)