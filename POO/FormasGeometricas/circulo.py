import math
from formaplana import FormaPlana as FP

class Circulo(FP):
  def __init__(self, raio):
    self.raio = raio

  def area (self):
    return math.pi * self.raio**2

  def perimetro(self):
    return 2 * math.pi * self.raio