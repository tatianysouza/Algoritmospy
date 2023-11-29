d1 = {'Processador':"250.50",
 'Memória RAM':"500.25",
 'HDD': "299.99",
 'SSD':"399.00",
 'Monitor':"1000.19",
 'Teclado':"50.00",
 'Mouse':"30.00"}

cont=True
while cont:
  a = input('Informe o produto: ')
  if a == 'Processador':
   print(f'Preço do {a}:', d1.get('Processador'))
  elif a == 'Memória RAM':
   print(f'Preço do {a}:', d1.get('Memória RAM'))
  elif a == 'HDD':
   print(f'Preço do {a}:', d1.get('HDD'))
  elif a == 'SSD':
   print(f'Preço do {a}:', d1.get('SSD'))
  elif a == 'Monitor':
   print(f'Preço do {a}:', d1.get('Monitor'))
  elif a == 'Teclado':
   print(f'Preço do {a}:', d1.get('Teclado'))
  elif a == 'Mouse':
   print(f'Preço do {a}:', d1.get('Mouse'))
  elif a == 'FIM':
   print('Obrigado por visitar nossa loja. Volte sempre!')
   break
  else:
   print('produto não encontrado')