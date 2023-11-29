lista = []
print('Digite 5 números')
for i in range(5):  
  lista.append(int(input(f'Número {i+1}: ' ))) 
soma = 0 
vezes = 1 

for i in lista: 
 soma  +=  i
 vezes *= i
print (lista) 
print (soma)  
print (vezes)