from enum import Enum 

class Direcao(Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class Cobra: 
  comprimento = None
  direcao = None
  corpo = None
  tamanho_bloco = None
  cor = (255,255,0)
  tamanho_tela = None


  def __init__(self, tamanho_bloco, tamanho_tela): 
    self.tamanho_bloco = tamanho_bloco
    self.tamanho_tela = tamanho_tela
    self.surgir()


  def surgir(self): 
    self.comprimento = 3
    self.corpo = [(20,20),(20,40),(20,60)]
    self.direcao = Direcao.DOWN


  def desenhar(self, jogo, tela): 
    for segmento in self.corpo:
      jogo.draw.rect(tela, self.cor, (segmento[0],segmento[1],self.tamanho_bloco, self.tamanho_bloco))


  def movimento(self): 
    tamanho_corpo_atual = self.corpo[-1]
    if self.direcao == Direcao.DOWN:
      prox_tamanho_corpo = (tamanho_corpo_atual[0], tamanho_corpo_atual[1] + self.tamanho_bloco)
      self.corpo.append(prox_tamanho_corpo)
    elif self.direcao == Direcao.UP:
      prox_tamanho_corpo = (tamanho_corpo_atual[0], tamanho_corpo_atual[1] - self.tamanho_bloco)
      self.corpo.append(prox_tamanho_corpo)
    elif self.direcao == Direcao.RIGHT:
      prox_tamanho_corpo = (tamanho_corpo_atual[0] + self.tamanho_bloco, tamanho_corpo_atual[1])
      self.corpo.append(prox_tamanho_corpo)
    elif self.direcao == Direcao.LEFT:
      prox_tamanho_corpo = (tamanho_corpo_atual[0] - self.tamanho_bloco, tamanho_corpo_atual[1])
      self.corpo.append(prox_tamanho_corpo)

    if self.comprimento < len(self.corpo):
      self.corpo.pop(0)


  def dirigir(self, direcao):
    if self.direcao == Direcao.DOWN and direcao != Direcao.UP:
      self.direcao = direcao
    elif self.direcao == Direcao.UP and direcao != Direcao.DOWN:
      self.direcao = direcao
    elif self.direcao == Direcao.LEFT and direcao != Direcao.RIGHT:
      self.direcao = direcao
    elif self.direcao == Direcao.RIGHT and direcao != Direcao.LEFT:
      self.direcao = direcao


  def comer(self):
    self.comprimento += 1

  def comida(self, comida):
    tamanho_cabeca = self.corpo[-1]
    if tamanho_cabeca[0] == comida.x and tamanho_cabeca[1] == comida.y:
        self.comer()
        return True
    return False


  def cauda(self):
    tamanho_corpo = self.corpo[-1]
    comer_cauda = False

    for i in range(len(self.corpo) - 1):
      segmento = self.corpo[i]
      if tamanho_corpo[0] == segmento[0] and tamanho_corpo[1] == segmento[1]:
        comer_cauda = True

    return comer_cauda


  def verificar_tam_tela(self):
    tamanho_corpo = self.corpo[-1]
    if tamanho_corpo[0] >= self.tamanho_tela[0]:
      return True
    if tamanho_corpo[1] >= self.tamanho_tela[1]:
      return True

    if tamanho_corpo[0] < 0:
        return True
    if tamanho_corpo[1] < 0:
        return True

    return False