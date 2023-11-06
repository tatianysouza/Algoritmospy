from pessoa import Pessoa as P

class Cliente(P):
  def __init__(self, nome, idade):
    super().__init__(nome, idade)