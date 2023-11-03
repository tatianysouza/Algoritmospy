import pygame
import random
from cobra import Cobra, Direcao
from comida import Comida
import sys

pygame.init()
tamanho_tela = (500, 420)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("JOGO DA COBRINHA")

azul = (0, 0, 255)
tamanho_bloco = 20
cobra = Cobra(tamanho_bloco, tamanho_tela)
comida = Comida(tamanho_bloco, tamanho_tela)
fonte = pygame.font.SysFont('Arial', 30, True)
score = 0  # Variável para acompanhar a pontuação

correr = True
clock = pygame.time.Clock()

while correr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cobra.dirigir(Direcao.LEFT)
    elif keys[pygame.K_RIGHT]:
        cobra.dirigir(Direcao.RIGHT)
    elif keys[pygame.K_UP]:
        cobra.dirigir(Direcao.UP)
    elif keys[pygame.K_DOWN]:
        cobra.dirigir(Direcao.DOWN)

    cobra.movimento()
    if cobra.comida(comida):
        score += 1
        comida.surgir()

    if cobra.verificar_tam_tela() or cobra.cauda():
        texto = fonte.render('Fim do jogo. Pontuação: %s' % score, True, (255, 255, 255))
        tela.blit(texto, (50, 200))
        pygame.display.update()
        pygame.time.delay(1000)
        cobra.surgir()
        comida.surgir()
        score = 0

    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, azul, [0, 0, 499, 419], 3)
    cobra.desenhar(pygame, tela)
    comida.desenhar(pygame, tela)
    pontos = fonte.render('Pontuação: %s' % score, True, (255, 255, 0))
    tela.blit(pontos, (10, 10))
    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()
