from forma3d import Forma3D as FD

class Paralelepipedo(FD):
  def __init__(self, lado1, lado2, lado3):
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3

  def volume(self):
    return self.lado1 * self.lado2 * self.lado3

  def diagonal(self):
    return self.lado1 **2 + self.lado2 **2 + self.lado3 **2