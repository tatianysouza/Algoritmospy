
from calculadora import Calculadora as C

print('-------Calculadora--------')
print('1-Adição')
print('2-Subtração')
print('3-Multiplicação')
print('4-Divisão')
print('5-Potenciação')
print('6-Ultimos Resultados')
print('7-Sair')
print('--------------------------')

lista = []

while True:
  y = input('-->Digite a opção escolhida: ')
  
  if y == '1':
    a = float(input('Primeiro número: '))
    b = float(input('Segundo número: '))
    x = C(a, b)
    x.soma()

    w = a+b    
    lista.append(w)

  elif y == '2':
    a = float(input('Primeiro número: '))
    b = float(input('Segundo número: '))
    x = C(a, b)
    x.subtracao()

    w = a-b
    lista.append(w)

  elif y == '3':
    a = float(input('Primeiro número: '))
    b = float(input('Segundo número: '))
    x = C(a, b)
    x.vezes()

    w = a*b
    lista.append(w)
  
  elif y == '4':
    a = float(input('Primeiro número: '))
    b = float(input('Segundo número: '))
    if b == 0:
      print('Impossivel divisão por 0')
    else:
      x = C(a, b)
      x.divisao()

      w = a/b
      lista.append(w)
 
  elif y == '5':
    a = float(input('Primeiro número: '))
    b = float(input('Segundo número: '))
    x = C(a, b)
    x.potenciacao() 

    w = a**b
    lista.append(w)

  elif y == '6':
    print(lista)

  elif y == '7':
    break

  else:
    print('Digite um valor válido')



