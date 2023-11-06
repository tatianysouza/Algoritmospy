from conta import Conta as C 

class ContaPoupanca(C):
  def __init__(self, agencia, conta, saldo):
    super().__init__(agencia, conta, saldo)

  def sacar(self, valor):
    if(self.saldo < valor):
      print('Não tem saldo para o saldo, na conta poupança')
      return
    self.saldo -= valor
    self.detalhes()