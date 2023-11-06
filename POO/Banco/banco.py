from cliente import Cliente as C

class Banco:
  def __init__(self, cliente):
    self._cliente = cliente
    self._contas = []

  def adicionar_conta(self, conta):
    self._contas.append(conta)

  def get_cliente(self):
    return self._cliente

  def get_contas(self):
    return self._contas