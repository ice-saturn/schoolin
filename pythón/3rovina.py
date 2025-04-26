# A[x, y]
# B[x, y]

#Ax, Ay = 5, 2
#Bx, By = 7, 10

Ax = 5
Ay = 2
Bx = 7
By = 10

A = [5, 2]
B = [7, 10]

def vzdalenostBodu(Ax, Ay, Bx, By) -> float:
   AxBx = abs(Ax - Bx)
   AyBy = abs(Ay - By)
   #je to prostě pythagorova věta
   return (AxBx ** 2 + AyBy ** 2) ** 0.5

def vzdalenostBodu2(A, B) -> float:
   #A[0] = 1.číslo, A[1] = 2.číslo
   AxBx = abs(A[0] - B[0])
   AyBy = abs(A[1] - B[1])
   return (AxBx ** 2 + AyBy ** 2) ** 0.5

#def vzdalenostBodu3(A, B) -> float:
   #A[0] = 1.číslo, A[1] = 2.číslo
   AxBx = abs(A["x"] - B["x"])
   AyBy = abs(A["y"] - B["y"])
   return (AxBx ** 2 + AyBy ** 2) ** 0.5


#A = {"x": 3,"y": 0}
#B = {"x": 4,"y": 0}

print(vzdalenostBodu(Ax, Ay, Bx, By))
print(vzdalenostBodu(0, 3, 4, 0))

print(vzdalenostBodu2(A, B))
print(vzdalenostBodu2([0, 3], [4, 0]))

#print(vzdalenostBodu3({"y": 3, "x":0}, {"x":4, "y":0}))