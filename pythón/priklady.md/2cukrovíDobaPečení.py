def sectiCukrovi(*argv):
    soucet = 0
    for arg in argv:
        soucet += arg 
    return soucet

koule = 15
rohlicky = 13
hnizda = 30
kokosky = 10
koule = 25

print(sectiCukrovi(koule, rohlicky, hnizda))