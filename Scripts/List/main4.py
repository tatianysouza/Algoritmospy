vogal = 0
consoante = 10
lista = []
print('Digite os caracteres')
for i in range(10):
  lista.append(str(input(f'caractere {i+1}: ')))
  letra = lista[i]
  if(letra=='a'):
    vogal+=1
  if(letra=='e'):
    vogal+=1
  if(letra=='i'):
    vogal+=1
  if(letra=='o'):
    vogal+=1
  if(letra=='u'):
    vogal+=1

print(f'Foram digitadas {vogal} vogais')
print(f'Foram digitadas {consoante-vogal} consoantes')