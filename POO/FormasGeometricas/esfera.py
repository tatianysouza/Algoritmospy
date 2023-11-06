import math
from forma3d import Forma3D as FD

class Esfera(FD):
  def __init__(self, raio):
    self.raio = raio

  def volume(self):
    return 4/3 * math.pi * self.raio**3