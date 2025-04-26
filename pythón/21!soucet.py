# fce soudet
# soucet řady čísel do 0 do n
n = int(input("Zadej číslo z kterého bude součet řad od 0 do nej: "))
def soucet(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + soucet(n - 1)

print(f"Součet řady od 0 do {n} je: {soucet(n)}")