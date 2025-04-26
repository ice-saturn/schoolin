def vyřešObjemKoule(poloměr):

 return (4/3) * 3.1415926535879 * poloměr ** 3 if poloměr > 0 else False

objem = 1     
while objem:
    objem = vyřešObjemKoule(float(input("Zadej poloměr Koule: ")))
    print(objem)
    
r1, r2, r3 = 17, 3.5, 21.7

print(vyřešObjemKoule(r1))
print(vyřešObjemKoule(r2))
print(vyřešObjemKoule(r3))