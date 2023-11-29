l1 = []
cont = 0
while(cont<5):
  a = int(input('Digite um número: '))
  if a%2==1:
    l1.append(a)
    cont = cont+1
  elif cont==5:
    break
    
t1=tuple(l1)
print(t1)

media = 0
for i in range(5):
  media +=t1[i]
media = media/5

print(f' A media entre todos os valores da tupla é: {media}')