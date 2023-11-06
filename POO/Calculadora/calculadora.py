class Calculadora:
  def __init__(self, n1, n2):
    self.n1 = float(n1)
    self.n2 = float(n2)

  def soma(self):
    mais = self.n1 + self.n2
    print(f'Resposta = {mais}')

  def subtracao(self):
    menos = self.n1 - self.n2
    print(f'Resposta = {menos}')

  def vezes(self):
    multiplicacao = self.n1 * self.n2
    print(f'Resposta = {multiplicacao}')

  def divisao(self):
    dividir = self.n1 / self.n2
    print(f'Resposta = {dividir}')

  def potenciacao(self):
    potencia = self.n1**self.n2
    print(f'Resposta = {potencia}')
