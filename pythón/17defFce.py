def zamen(slovo, pozice, novy_znak):
    """V daném slově zamění znak na dané pozici za daný nový znak."""
    zacatek = slovo[:pozice]
    konec = slovo[pozice + 1:]
    nove_slovo = zacatek + novy_znak + konec
    return nove_slovo

print(zamen('kočka', 1, 'a'))
print(zamen('kačka', 2, 'p'))

def napis_hlasku(nazev, skore):
    """Popíše skóre. Název má být přivlastňovací přídavné jméno."""

    print(nazev, 'skóre je', skore)
    if skore > 1000:
        print('Světový rekord!')
    elif skore > 100:
        print('Skvělé!')
    elif skore > 10:
        print('Ucházející.')
    elif skore > 1:
        print('Aspoň něco')
    else:
        print('Snad příště.')

napis_hlasku('Tvoje', 256)
napis_hlasku('Protivníkovo', 5)


def obsah_obdelnika(a, b):
    return a * b

print ("Obsah obdelníka se stranami 3 cm a 5 cm je", obsah_obdelnika(3, 5), "cm2")

def ano_nebo_ne(otazka):
#    """Vrátí True nebo False podle odpovědi uživatele"""
    while True:
        odpoved = input(otazka)
        if odpoved == 'ano':
            return True
        elif odpoved == 'ne':
            return False

        print('Nerozumím! Odpověz "ano" nebo "ne".')


# Příklad použití
if ano_nebo_ne('Chceš si zahrát hru? '):
    print('OK! Ale napřed si ji musíš naprogramovat.')
else:
    print('Škoda.')