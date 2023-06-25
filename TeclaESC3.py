import pygame
import sys
from pygame.locals import *
from tkinter import Tk, simpledialog
import pickle
import math

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

def save_stars():
    try:
        with open('stars.pkl', 'wb') as f:
            pickle.dump(stars, f)
    except IOError:
        print("Erro ao salvar as marcações.")

def load_stars():
    global stars
    try:
        with open('stars.pkl', 'rb') as f:
            stars = pickle.load(f)
    except FileNotFoundError:
        print("Arquivo de marcações não encontrado.")
        stars = []

def delete_stars():
    global stars
    stars = []

def get_star_name():
    root = Tk()
    root.withdraw()
    star_name = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return star_name

def calculate_distance(star1, star2):
    x1, y1 = star1[0]
    x2, y2 = star2[0]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def draw_stars():
    for i in range(len(stars)):
        pos, name = stars[i]
        pygame.draw.circle(screen, RED, pos, 5)
        font = pygame.font.SysFont(None, 20)
        
        if name == "Desconhecido":
            text = font.render(name, True, RED)
            text_rect = text.get_rect(center=pos)
            screen.blit(text, text_rect)
            
            # Exibir coordenadas ao lado do texto "Desconhecido"
            coord_text = font.render(f"({pos[0]}, {pos[1]})", True, RED)
            coord_text_rect = coord_text.get_rect(left=text_rect.right + 5, centery=text_rect.centery)
            screen.blit(coord_text, coord_text_rect)
        else:
            text = font.render(name, True, RED)
            text_rect = text.get_rect(center=pos)
            screen.blit(text, text_rect)
            
        if i > 0:
            prev_pos, _ = stars[i-1]
            pygame.draw.line(screen, RED, prev_pos, pos, 1)
            
    # Exibir distâncias entre as marcações
    for i in range(1, len(stars)):
        star1 = stars[i-1]
        star2 = stars[i]
        distance = calculate_distance(star1, star2)
        pos = (star1[0][0] + (star2[0][0] - star1[0][0]) // 2, star1[0][1] + (star2[0][1] - star1[0][1]) // 2)
        font = pygame.font.SysFont(None, 18)
        text = font.render(f"{distance:.2f}", True, RED)
        text_rect = text.get_rect(center=pos)
        screen.blit(text, text_rect)

# Carregar marcações salvas (se existirem)
load_stars()

running = True
while running:
    # Limpeza da tela
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            # Salvar as marcações antes de fechar
            save_stars()
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Capturar a posição do clique do mouse
            mouse_pos = pygame.mouse.get_pos()

            # Abrir caixa de diálogo para obter o nome da estrela
            star_name = get_star_name()
            if star_name:
                if not star_name.strip():
                    star_name = "Desconhecido"
                stars.append((mouse_pos, star_name))
        elif event.type == KEYDOWN:
            if event.key == K_F10:
                save_stars()
            elif event.key == K_F11:
                load_stars()
            elif event.key == K_F12:
                delete_stars()
            elif event.key == K_ESCAPE:
                # Salvar as marcações ao pressionar a tecla ESC
                save_stars()

    draw_stars()

    # Atualização da tela
    pygame.display.flip()
    clock.tick(60)

# Finalização do Pygame
pygame.quit()
sys.exit()
