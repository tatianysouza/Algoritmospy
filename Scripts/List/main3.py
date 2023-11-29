media= 0
lista = []
print('Digite suas 4 notas')
for i in range(4):
  lista.append(int(input(f'Nota {i+1}: ')))
  media += lista[i]
media = media/4
print(f'Sua média foi {media}')