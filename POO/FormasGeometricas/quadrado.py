from formaplana import FormaPlana as FP

class Quadrado(FP):
  def __init__(self, lado):
    self.lado = lado

  def area(self):
    return self.lado **2

  def diagonal(self):
    return self.lado*(2**(1/2))

  def perimetro(self):
    return self.lado *4