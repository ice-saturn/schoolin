# faktoriál čísla pomocí for

cislo_for = int(input("Číslo z kterého chcete faktoriá (pomocí for): "))
def faktorial_for(cislo_for):
    vysledek = 1
    for i in range(1, 1 + cislo_for):
        vysledek *= i
    return vysledek

print(f"Faktoriál čísla {cislo_for} (pomocí for) je: {faktorial_for(cislo_for)}")

# faktoriál čísla pomocí rekurze

cislo_rek = int(input("Číslo z kterého chcete faktoriá (pomocí rekurze): "))
def faktorial_rek(cislo_rek):
    if cislo_rek == 0 or cislo_rek == 1:
        return 1
    else:
        return cislo_rek * faktorial_rek(cislo_rek - 1)

print(f"Faktoriál čísla {cislo_rek} (pomocí rekurze) je: {faktorial_rek(cislo_rek)}")