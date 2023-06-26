import pygame
import sys
from pygame.locals import *
from tkinter import Tk, simpledialog
import pickle
import math


WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Marker")
clock = pygame.time.Clock()

icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)


background_image = pygame.image.load("bg.jpg")


pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)  

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
    if star_name is None or star_name.strip() == "":
        #messagebox.showinfo("Nome Inválido", "O nome da estrela não pode estar vazio. Será usado o nome 'Desconhecido'.")
        star_name = "Desconhecido"
    return star_name

def calculate_distance(star1, star2):
    x1, y1 = star1[0]
    x2, y2 = star2[0]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

def draw_stars():
    for i in range(len(stars)):
        pos, name = stars[i]
        pygame.draw.circle(screen, WHITE, pos, 5)
        font = pygame.font.SysFont(None, 20)
        
        if name == "Desconhecido":
            text = font.render(name, True, WHITE)
            text_rect = text.get_rect(center=(pos[0], pos[1] - 15))
            screen.blit(text, text_rect)
            
        
            coord_text = font.render(f"({pos[0]}, {pos[1]})", True, WHITE)
            coord_text_rect = coord_text.get_rect(left=text_rect.right + 5, centery=text_rect.centery)
            screen.blit(coord_text, coord_text_rect)
            
        else:
            text = font.render(name, True, WHITE)
            text_rect = text.get_rect(center=(pos[0], pos[1] - 15))
            screen.blit(text, text_rect)
            
        if i > 0:
            prev_pos, _ = stars[i-1]
            pygame.draw.line(screen, WHITE, prev_pos, pos, 1)
            
         
            distance = calculate_distance(stars[i-1], stars[i])
            distance_text = font.render(f"{distance:.2f}", True, WHITE)
            distance_text_rect = distance_text.get_rect(center=((prev_pos[0] + pos[0]) // 2, (prev_pos[1] + pos[1]) // 2 - 15))
            screen.blit(distance_text, distance_text_rect)
    
    
    font = pygame.font.SysFont(None, 18)
    f10_text = font.render("F10 - Salvar", True, WHITE)
    f10_rect = f10_text.get_rect(top=10, left=10)
    screen.blit(f10_text, f10_rect)
    
    f11_text = font.render("F11 - Carregar", True, WHITE)
    f11_rect = f11_text.get_rect(top=f10_rect.bottom + 5, left=10)
    screen.blit(f11_text, f11_rect)
    
    f12_text = font.render("F12 - Apagar", True, WHITE)
    f12_rect = f12_text.get_rect(top=f11_rect.bottom + 5, left=10)
    screen.blit(f12_text, f12_rect)



load_stars()

running = True
while running:
    
    screen.fill(WHITE)

   
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        try:
            if event.type == QUIT:
                save_stars()
                pygame.mixer.music.stop()  
                running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                star_name = get_star_name()
                stars.append((mouse_pos, star_name))
            elif event.type == KEYDOWN:
                if event.key == K_F10:
                    save_stars()
                elif event.key == K_F11:
                    load_stars()
                elif event.key == K_F12:
                    delete_stars()
                elif event.key == K_ESCAPE:
                    # Salvar as marcações e gerar evento de encerramento
                    save_stars()
                    pygame.event.post(pygame.event.Event(QUIT))
        except Exception as e:
            print("Erro no tratamento de eventos:", e)

    draw_stars()

    # Exibir coordenadas cartesianas
    font = pygame.font.SysFont(None, 18)
    #for pos, _ in stars:
        #coord_text = font.render(f"({pos[0]}, {pos[1]})", True, WHITE)
        #coord_text_rect = coord_text.get_rect(top=pos[1] + 10, left=pos[0] - 20)
        #screen.blit(coord_text, coord_text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
