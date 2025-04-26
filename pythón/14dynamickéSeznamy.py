import random

pokus = []
velikost = int(input("Zadejte velikost pole: ")) #kolik gamb chceš(1-10)

for i in range(velikost):
    pokus.append(random.randint(0,10))
print(pokus)