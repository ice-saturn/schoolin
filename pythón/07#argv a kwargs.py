def pocitej(**kwargs):
    c = kwargs["cisla"] # pole čísel, např. [1, 2, 3, 4, 15]
    o = kwargs["operace"] # mic, max avg
    
    if (o == "min"):
        return min(c)
    elif (o == "max"):
        return max(c)
    elif (o == "avg"):
        return sum(c)/len(c)
    else:
        return False

min = pocitej(cisla = [2, 3, 5, 7, 11, 13, 17, 19, 23], operace="min")
max = pocitej(cisla = [2, 3, 5, 7, 11, 13, 17, 19, 23], operace="max")
avg = pocitej(cisla = [2, 3, 5, 7, 11, 13, 17, 19, 23], operace="avg")

print(min, max, avg)