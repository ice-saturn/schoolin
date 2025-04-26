# 2. Zapište funkci, která bude počítat celkovou cenu vstupenek do kina. 
# Cena vstupenek je v kině stanovena na:
# - dětská……85,-
# - dospělá….150,-
# - senior…70,-
# V programu zadejte vždy určitý počet vstupenek pro dítě, dospělého i seniora. 
# Vypočítejte celkovou cenu za hromadnou vstupenku. 
# V ceně vstupenky se také zahrne následující:
# - pokud bude celková cena větší než 1000,-, obdržíte slevu 20%
# - celková cena pak bude nižší právě o 20%“


def celkova_cena_vstupenek(detska, dopsela, senior):
    detska_cena = 85
    dospela_cena = 150
    senior_cena = 70
    
    celkova_cena = (detska * detska_cena) + (dospela * dospela_cena) + (senior * senior_cena)
    
    if celkova_cena > 1000:
        celkova_cena/(5*4)
    
    return celkova_cena

detska = 3
dospela = 2
senior = 1

celkova_cena = celkova_cena_vstupenek(detska, dospela, senior)

print(celkova_cena)