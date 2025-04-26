def jsouVánoce(den,měsíc):
    if měsíc == 12 and (den == 25 or den == 26):
        return f"{den}.{měsíc}. Jsou Vánoce!"
    else:
        return f"{den}.{měsíc}. Nejsou Vánoce :c"
print(jsouVánoce(25, 11))