import pygame
import sys
from pygame.locals import *

# Configurações da tela
WIDTH = 800
HEIGHT = 600

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicialização do Pygame
pygame.init()

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Marker")
clock = pygame.time.Clock()

# Lista para armazenar as estrelas marcadas
stars = []


def draw_stars():
    for star in stars:
        pygame.draw.circle(screen, RED, star, 5)


running = True
while running:
    # Limpeza da tela
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Capturar a posição do clique do mouse
            mouse_pos = pygame.mouse.get_pos()
            stars.append(mouse_pos)

    draw_stars()

    # Atualização da tela
    pygame.display.flip()
    clock.tick(60)

# Finalização do Pygame
pygame.quit()
sys.exit()
