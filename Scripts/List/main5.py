lista = []
listai = []
listap = []
number = 0
print('Digite 20 números')
for i in range(20):
  lista.append(int(input(f'Number {i+1}: ')))
  number=lista[i]
  if(number%2==0):
    listap.append(number)
  else:
    listai.append(number)

print(listap)
print(listai)
print(lista)