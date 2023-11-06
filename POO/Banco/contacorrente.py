from conta import Conta as C 

class ContaCorrente(C):
  def __init__(self, agencia, conta, saldo, limite = 950):
    super().__init__(agencia, conta, saldo)
    self._limite = limite

  @property
  def limite(self):
    return self._limite

  def sacar(self, valor):
    if(self.saldo + self._limite) < valor:
      print('Não tem saldo para saque')
      return
    self.saldo -= valor
    self.detalhes()