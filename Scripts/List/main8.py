import random
lista = []
listaimpar = []
for i in range(10):
 x = random.randrange(1,100)
 lista.append(x)
 if x%2 == 1:
  listaimpar.append(x)

print(lista)
print(listaimpar)