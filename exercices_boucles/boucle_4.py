import random
ma_liste = [ random.randint(0, 10000)  for _ in range(1000) ]

haut = 0
for n in ma_liste:
    if n > haut:
        haut = n
print (haut)
