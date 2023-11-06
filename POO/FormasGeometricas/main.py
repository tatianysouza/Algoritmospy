from quadrado import Quadrado as Q
from circulo import Circulo as C
from retangulo import Retangulo as R
from cubo import Cubo as CB
from esfera import Esfera as E
from paralelepipedo import Paralelepipedo as P


while True:
  print('--------------------------')
  print('1-Quadrado') 
  print('2-Circulo')
  print('3-Retângulo')
  print('4-Cubo')
  print('5-Esfera')
  print('6-Paralelepipedo')
  print('7-Sair')
  print('--------------------------')
  x = input('Digite a opção escolhida: ')

  if x == '1':
    a = int(input('Informe o lado da forma: '))
    q1 = Q(a)
    print('-------------------------')
    print('1-Área')
    print('2-Diagonal')
    print('3-perimetro')
    print('4-Todos')
    print('-------------------------')
    y = input('Digite a opção escolhida: ')

    if y == '1':
      print('----------------------------\n')
      q1.areafp()
      print(f'Área = {q1.area() }\n')
    elif y =='2':
      print('----------------------------\n')
      q1.diagonalfp()
      print(f'Diagonal = {q1.diagonal()}\n')
    elif y == '3':
      print('----------------------------\n')
      q1.perimetrofp()
      print(f'Perimetro = {q1.perimetro()}\n')
    elif y == '4':
      print('----------------------------\n')
      q1.descricao()
      print(f'Área = {q1.area() }')
      print(f'Diagonal = {q1.diagonal()}')
      print(f'Perimetro = {q1.perimetro()}\n')
    else:
      print('----------------------------')
      print('Digite um número válido\n')
      z = input('Digite a opção escolhida: ')
  elif x =='2':
    a = int(input('Informe o raio da forma: '))
    c1 = C(a)
    print('-------------------------')
    print('1-Área')
    print('2-perimetro')
    print('3-Todos')
    print('-------------------------')
    y = input('Digite a opção escolhida: ')
    if y == '1':
      print('----------------------------\n')
      c1.areafp()
      print(f'Área = {c1.area()}\n')
    elif y == '2':
      print('----------------------------\n')
      c1.perimetrofp()
      print(f'Perimetro = {c1.perimetro()}\n')
    elif y == '3':
      print('----------------------------\n')
      c1.descricao()
      print(f'Área = {c1.area()}')
      print(f'Perimetro = {c1.perimetro()}\n')
    else:
      print('-----------------------------')
      print('Digite um número válido\n')
  elif x == '3':
    a = int(input('Informe o lado 1 da forma: '))
    b = int(input('informe o lado 2 da forma: '))
    r1 =R(a,b)
    print('-------------------------')
    print('1-Área')
    print('2-perimetro')
    print('3-Diagonal')
    print('4-Todos')
    print('-------------------------')
    y = input('Digite a opção escolhida: ')
    if y == '1':
      print('----------------------------\n')
      r1.areafp()
      print(f'Área = {r1.area()}\n')
    elif y == '2':
      print('----------------------------\n')
      r1.perimetrofp()
      print(f'Perimetro = {r1.perimetro()}\n')
    elif y == '3':
      print('----------------------------\n')
      r1.diagonalfp()
      print(f'Diagonal = {r1.diagonal()}\n')
    elif y == '4':
      print('----------------------------\n')
      r1.descricao()
      print(f'Área = {r1.area() }')
      print(f'Diagonal = {r1.diagonal()}')
      print(f'Perimetro = {r1.perimetro()}\n')
    else:
      print('-----------------------------')
      print('Digite um número válido\n')

  elif x == '4':
    a = int(input('Informe o lado da forma: '))
    cb1 = CB(a)
    print('-------------------------')
    print('1-Volume')
    print('2-Diagonal')
    print('3-Todos')
    print('-------------------------')
    z = input('Digite a opção escolhida: ')
    if z == '1':
      print('----------------------------\n')
      cb1.volumefd()
      print(f'Volume = {cb1.volume()}\n')
    elif z == '2':
      print('----------------------------\n')
      cb1.diagonalfd()
      print(f'Diagonal = {cb1.diagonal()}\n')
    elif z == '3':
      print('----------------------------\n')
      cb1.descricaofd()
      print(f'Volume = {cb1.volume()}')
      print(f'Diagonal = {cb1.diagonal()}\n')
    else:
      print('-----------------------------')
      print('Digite uma opção valida')
  elif x == '5':
    a = int(input('Informe o raio da forma: '))
    e1 = E(a)
    print('-------------------------')
    e1.volumefd()
    print(f'volume = {e1.volume()}\n')
  elif x == '6':
    a = int(input('informe o lado 1 da forma: '))
    b = int(input('informe o lado 2 da forma: '))
    c = int(input('informe o lado 3 da forma: '))
    p1 = P(a,b,c)
    print('-------------------------')
    print('1-Volume')
    print('2-Diagonal')
    print('3-Todos')
    print('-------------------------')
    z = input('Digite a opção escolhida: ')
    if z == '1':
      print('----------------------------\n')
      p1.volumefd()
      print(f'Volume = {p1.volume()}\n')
    elif z == '2':
      print('----------------------------\n')
      p1.diagonalfd()
      print(f'Diagonal = {p1.diagonal()}\n')
    elif z == '3':
      print('----------------------------\n')
      p1.descricaofd()
      print(f'Volume = {p1.volume()}')
      print(f'Diagonal = {p1.diagonal()}\n')
    else:
      print('-----------------------------')
      print('Digite um valor válido')
  elif x =='7':
    break
  else:
    print('Digite um número válido')
    
    