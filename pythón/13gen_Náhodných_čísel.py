##Vygeneruje náhodné číslo v rozsahu 1-10
#import random
#random.randint(0,10)

import random

pokus, pokus2, pokus3 = [], [], []

for i in range(10):
    pokus.append(random.randint(0,10))
    pokus2.insert(i, random.randint(0,10))
    pokus3.append(random.uniform(0.1,1.6))

print(pokus)
print(pokus2)
print(pokus3)