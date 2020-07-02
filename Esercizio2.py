from random import *

Matrice = [[],
           [],
           [],
           []]
i = 0
j = 0

while i < len(Matrice):
    j = 0
    while j < len(Matrice):
        Matrice[i].append(randint(1, 10))
        j = j + 1
    i = i +1

print(f'Matrice: {Matrice}')

medie = []

s = 0
i = 0
j = 0

while i < len(Matrice):
    j = 0
    s = 0
    while j < len(Matrice):
        s = s + Matrice[i][j]
        j = j + 1
    medie.append(s/len(Matrice))
    i = i + 1

i = 0

while i < len(Matrice):
    print(f'Media {Matrice[i]} : {medie[i]}')
    i = i + 1


