lista = []
print('Digite 10 números reais')
for i in range(10):
  lista.append(input(f'Número {i+1}: '))
lista.sort()
lista.reverse()
print(lista)