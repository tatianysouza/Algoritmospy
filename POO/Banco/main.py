from cliente import Cliente as C
from banco import Banco as B
from pessoa import Pessoa as P
from contacorrente import ContaCorrente as CC
from contapoupanca import ContaPoupanca as CP

banco = None

while True:
  print('--------------------------')
  print('1-Criar Cliente') 
  print('2-Criar Conta')
  print('3-Ver Detalhes da Conta')
  print('4-Sacar Dinheiro')
  print('5-Depositar Dinheiro')
  print('6-Sair')
  print('--------------------------')
  x = input('Digite a opção escolhida: ')

  if x == '1':
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    cliente = C(nome, idade)
    banco = B(cliente)

  elif x == '2':
    agencia = input('Agencia: ')
    numero_conta = input('Conta: ')
    saldo = float(input('Saldo: '))
    tipo_conta = input('Tipo de Conta (poupanca/corrente): ')
    if tipo_conta.lower() == 'poupanca':
      conta = CP(agencia, numero_conta, saldo)
    else:
      conta = CC(agencia, numero_conta, saldo)
    banco.adicionar_conta(conta)

  elif x == '3':
    for conta in banco.get_contas():
      conta.detalhes()

  elif x == '4':
    numero_conta = input('Número da Conta: ')
    valor = float(input('Valor a Sacar: '))
    for conta in banco.get_contas():
      if conta.conta == numero_conta:
        conta.sacar(valor)

  elif x == '5':
    numero_conta = input('Número da Conta: ')
    valor = float(input('Valor a Depositar: '))
    for conta in banco.get_contas():
      if conta.conta == numero_conta:
        conta.depositar(valor)

  elif x == '6':
    break
  else: 
    print('Opção inválida')
