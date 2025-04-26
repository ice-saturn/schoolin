cislo = int(input("Zadej desítkové celé číslo: "))
soustava = 2
seznam = []
while cislo > 0:
    seznam.insert(0, cislo % soustava)
    cislo = cislo // soustava
print (seznam)