import pygame
import sys
from pygame.locals import *
from tkinter import Tk, simpledialog

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


def get_star_name():
    root = Tk()
    root.withdraw()
    star_name = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return star_name


def draw_stars():
    for star in stars:
        pygame.draw.circle(screen, RED, star[0], 5)
        font = pygame.font.SysFont(None, 20)
        text = font.render(star[1], True, RED)
        text_rect = text.get_rect(center=star[0])
        screen.blit(text, text_rect)


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

            # Abrir caixa de diálogo para obter o nome da estrela
            star_name = get_star_name()
            if star_name:
                stars.append((mouse_pos, star_name))

    draw_stars()

    # Atualização da tela
    pygame.display.flip()
    clock.tick(60)

# Finalização do Pygame
pygame.quit()
sys.exit()
