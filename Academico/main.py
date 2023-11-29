def sistema_academico():
  print('-- Sistema Acadêmico --')
  print()
  print('1-cadastrar')
  print('2-pesquisar')
  print('3-listar')
  print('4-atualizar')
  print('5-remover')
  print('6-encerrar')
  print()

  opcao = int(input('Digite uma opção: '))
  return opcao 

def cadastro():
  print('-->Opção de cadastro')
  a = int(input('matrícula: '))
  b = input('Digite o nome: ')
  c = input('Informe o curso: ')
  d = float(input('Informe o CRE: '))
  x = {'matricula': a, 'nome':b, 'curso':c, 'media':d}
  return x

def pesquisar():
  print('-->Opção de pesquisa:')
  nome = input("Digite o nome que deseja buscar: ")
  for i in range(0, len(dic)):
    cl = dic[i]
    if (nome == cl['nome']):
      print(cl)
    else:
      print('Essa pessoa não possui cadastro')  

def listar():
  print('-->Opção de listar:')
  print(dic)
  print('cadastros')

def atualizar():
  print('-->Opção de atualizar:')
  nome = input('Digite o nome: ')
  matricula = input('Digite a matricula: ')
  curso = input('Digite o curso:')
  media = input('Digite o CRE: ')
  for i in range(0,len(dic)):
    pl = dic[i]
    if (nome == pl['nome']):
      pl['nome'] = nome
      pl['matricula'] = matricula
      pl['curso'] = curso
      pl['media'] = media
      print(pl)

def remover():
  print('-->Opção de excluir:')
  nome = input('Nome do cadastro que deseja excluir: ')
  for i in range(0,len(dic)):
    tl = dic[i] 
    x = tl
    if (nome == tl['nome']):
      dic.remove(x)
      print('Cadastro apagado com sucesso!')


def encerrar():
  if opcao == 6:
    print('--Você escolheu sair do programa--\n')


dic = {}
dic =[]
cond = True
while(cond):
  opcao = sistema_academico()
 
  if(opcao == 1):
    resultado = cadastro()
    print(f'--->Cadastro: {resultado}')
    dic.append(resultado)
    print('Cadastro feito com sucesso\n')
  
  elif(opcao == 2):
    pesquisar()

  elif(opcao == 3):
    listar()

  elif(opcao == 4):
    atualizar()

  elif(opcao == 5):
    remover()

  elif(opcao == 6):
    encerrar() 
    break

  else:
    print('--Opção Inválida--')