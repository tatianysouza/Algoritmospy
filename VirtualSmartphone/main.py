nome = input('Digite seu nome: ')
att = input(f'BEM VINDO\A ao celular virtual {nome}!')

def celular ():
  print('-------CELULAR VIRTUAL-------\n')
  print('1-caculadora')
  print('2-contatos')
  print('3-bloco de notas')
  print('4-Jogar')
  print('5-formatar\n')

  opcao = int(input('O que deseja acessar? '))
  print()
  return opcao

def calcular():
  print('-----------------------------')
  print('--> Opção calculadora')
  print('1-somar')
  print('2-subtrair')
  print('3-multiplicar')
  print('4-dividir')
  print('5-potência\n')
  tl = int(input('digite uma opcão: '))
  return tl

def soma():
  print('-----------------------------')
  print('-->Opção Soma:')
  n1 = float(input('Número 1: '))
  n2 = float(input('Número 2: '))
  somar = n1 + n2
  return somar

def menos():
  print('-----------------------------')
  print('-->Opção Subtração:')
  n1 = float(input('Número 1: '))
  n2 = float(input('Número 2: '))
  sub = n1 - n2
  return sub

def vezes():
  print('-----------------------------')
  print('-->Opção multiplicação')
  n1 = float(input('Número 1: '))
  n2 = float(input('Número 2: '))
  vz = n1*n2
  return vz

def divisao():
  print('-----------------------------')
  print('-->Opção divisão')
  n1 = float(input('Número 1: '))
  n2 = float(input('Número 2: '))
  div = n1/n2
  return div

def potencia():
  print('-----------------------------')
  print('-->Opção potência')
  n1 = float(input('Número 1: '))
  n2 = float(input('Número 2: '))
  pt = n1**n2
  return pt

conts = []

def contatos():
  print('-----------------------------')  
  print('--> Opcão contatos')
  print('1-Novo contato') 
  print('2-Pesquisar') 
  print('3-Mostrar todos') 
  print('4-Editar')
  print('5-Excluir')
  cl = int(input('Digite uma opção: '))
  return cl

def novo():
  print('-----------------------------')
  print('-->Novo Contato')
  a = input('Nome: ')
  b = int(input('Número: '))
  c = input('Email: ')
  x = {'nome': a, 'telefone': b, 'email':c}
  return x

def pesquisar():
  print('-----------------------------')
  print('-->Pesquisar:')
  nome = input("Digite do contato: ")
  for i in range(0, len(conts)):
    cl = conts[i]
    if (nome == cl['nome']):
      print(cl)

def todos():
  print('-----------------------------')
  print('-->Contatos')
  print(conts)

def editar():
  print('-----------------------------')
  print('-->Editar:')
  nome = input('Nome: ')
  numero = input('Numero: ')
  email = input('Email: ')
  for i in range(0,len(conts)):
    ed = conts[i]
    if (nome == ed['nome']):
      ed['nome'] = nome
      ed['telefone'] = numero
      ed['email'] = email
      print(ed)

def excluir():
  print('-----------------------------')
  print('-->Excluir')
  nome = input('Nome: ')
  for i in range(0,len(conts)):
    ex = conts[i] 
    x = ex
    if (nome == ex['nome']):
      conts.remove(x)
      print('Contato excluido')

def notas():
  print('-----------------------------')
  print('-->Bloco de notas')
  print('1-criar nota')
  print('2-ler nota')
  print('3-escrever')
  print('4-excluir\n')
  kl = int(input('Digite uma opção: '))
  return kl

def criar():
  print('-----------------------------')
  print('-->Criar nota')
  try:
    arquivo = open("nota.txt",'x')
    arquivo.close()
    print('Nota criada com sucesso')
  except:
    print('Nota já criada')

def ler():
  print('-----------------------------')
  print('-->ler nota')
  try:
    arquivo = open("nota.txt", 'r')
    print(arquivo.name, 'aberto com sucesso')
    while True:
      cont = arquivo.readline()
      print(cont, end='')
      if (cont == ''):
       break
    arquivo.close()
  except:
    print('Impossivel abrir')

def escrever():
  print('-----------------------------')
  print('-->Escrever')
  try:
    arquivo = open("nota.txt", 'a')
    a = input('Digite o que deseja: ')
    print(a, file=arquivo)
    print('Salvo com sucesso')
    arquivo.close()
  except:
    print('Não foi possivel abrir a nota')

def apagar():
  try:
    arquivo = open("nota.txt", 'w')
    arquivo.write("")
    print('-----------------------------')
    print('Conteúdo da nota apagado com sucesso')
  except:
    print('Não foi possivel abrir a nota')    

def jogo():

  import random
  print('-----------------------------')
  print('-->Joguinho do gênio da lâmpada\n')
  print(f'Como Jogar: {nome} faça uma pergunta sobre o que você deve fazer e o gênio responderá você.')
  print('Para sair do jogo digite fim\n')
  while True:
    x = input('Faça uma pergunta ao gênio: ')
    lista = ['Sim','Não','Talvez', 'Melhor não', 'Nem pensa nisso', 'Pq não?', 'Essa eu não sei te responder', 'claro', 'Tenta de novo']
    resposta = random.choice(lista)
    print(f'{x} = {resposta}\n')
    if x == 'fim':
      break

    
cond = True
while(cond):
  opcao = celular()

  if (opcao == 1):
    resul = calcular()
    if resul == 1:
      print(f'resultado = {soma()}\n')
    elif resul == 2:
      print(f'resultado = {menos()}\n')
    elif resul == 3:
      print(f'resultado = {vezes()}\n')
    elif resul == 4:
      print(f'resultado = {divisao()}\n')
    elif resul == 5:
      print(f'resultado = {potencia()}\n')
    else:
      print('-->Opção inválida')

  elif (opcao == 2):
    resul = contatos()
    if resul == 1:
      ppp = novo()
      print('-->Contato salvo')
      conts.append(ppp)
      
    elif resul == 2:
      pesquisar()

    elif resul == 3:
      todos()

    elif resul == 4:
      editar()  

    elif resul == 5:
      excluir()  
     
    else:
      print('Opção inválida')

  elif (opcao == 3):
    resul = notas()
    if resul == 1:
      criar()
    elif resul == 2:
      ler()
    elif resul == 3:
      escrever()
    elif resul == 4:
      apagar()

  elif (opcao == 4):
    resul = jogo()

  elif (opcao == 5):
    a = input('Tem certeza [s/n]? ')
    
    if a == 's':
      apagar()
      print('--Formatação completa--')
      break

  else:
    print('-->Opção inválida')
