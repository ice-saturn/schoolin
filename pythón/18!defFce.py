# 1. Zapiš funkci, která se bude jmenovat „prumerna_rychlost“ a která 
# bude počítat průměrnou rychlost ze zadané dráhy a celkového času. 
# Průměrná rychlost se vypočítá jako v=s/t. 
# [na vstupu zadáte dráhu (m) a čas (s)].

def prumerna_rychlost(draha,cas):
   
    if cas <= 0:
        return "Čas se nesmí být menší nebo se rovnat nule"
      
   
    v = draha/cas
    return v

draha = 30
cas = 12

v = prumerna_rychlost(draha,cas)
print(f"prumerna rychlost = {v}")