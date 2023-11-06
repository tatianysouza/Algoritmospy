from forma3d import Forma3D as FD

class Cubo(FD):
  def __init__(self, lado):
    self.lado = lado

  def volume (self):
    return self.lado **3

  def diagonal(self):
    return self.lado*(3**(1/2))