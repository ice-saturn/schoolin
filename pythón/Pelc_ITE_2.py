def mocnina(x, n):
    return x ** n

x = float(input("Zadejte základ mocniny (x): "))
n = int(input("Zadejte exponent (n): "))

vysledek = mocnina(x, n)
print(f"{n}-tá mocnina čísla {x} je: {vysledek}")