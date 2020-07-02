a = [[], [], [], [], []]
b = [[], [], [], [], []]


for i in range(5):
    a[i].append()
    for k in range(5):
        a[i].append()


cont = 0
for row in b:
    for el in row:
        if b == el.any():
            cont = cont+1

print(f'questi {cont} elementi corrispondono')