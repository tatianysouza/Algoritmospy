import random

class Comida:
    tamanho_bloco = None
    cor = (255,0,0)
    x = 0;  
    y = 0;
    tamanho_tela = None


    def __init__(self, tamanho_bloco, tamanho_tela):
      self.tamanho_bloco = tamanho_bloco
      self.tamanho_tela = tamanho_tela


    def desenhar(self, jogo, tela):  
      jogo.draw.rect(tela, self.cor, (self.x, self.y, self.tamanho_bloco, self.tamanho_bloco)) 


    def surgir(self):
      bloco_x = (self.tamanho_tela[0])/self.tamanho_bloco;
      bloco_y = (self.tamanho_tela[1])/self.tamanho_bloco;
      self.x = random.randint(0, bloco_x - 1) * self.tamanho_bloco
      self.y = random.randint(0, bloco_y - 1) * self.tamanho_bloco      
                        
