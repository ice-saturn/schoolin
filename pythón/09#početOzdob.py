#Zadání: Napište program, který pomůže spočítat, 
# kolik ozdob je potřeba na vánoční stromeček. 
# Uživatel zadá výšku stromku (v počtu řad). 
# Každá řada potřebuje dvojnásobek počtu ozdob oproti předchozí řadě,
# začíná se od jedné ozdoby v první řadě. Program vypíše celkový počet ozdob.

pocet_rad = int(input("Zadej počet řad: "))

#prvni_rada = 1
#druha_rada = 2 * prvni_rada
#treti_rada = 2 * druha_rada

#matika 3.třídy ☻ ↓
prvni_rada = 1
q = 2

#S = prvni_rada * (1 - q ** pocet_rad) / (1 - q)
#print(f"Počet ozdob je {S}")

pocet_kouli = 0
for i in range(pocet_rad):
    pocet_kouli += 2 ** i

print(f"Počet ozdob je {pocet_kouli}")