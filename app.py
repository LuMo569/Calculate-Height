from packeges.button import Button
import os
import pygame


# create project for Niklas group that...
# 1. Calculates
# 2. Let´s you play a fun little game with adequate features

# Current game is just a placeholder

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.init()

# Parameters
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("App")

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# load button images
start_img = pygame.image.load('assets/start_btn.png').convert_alpha()
exit_img = pygame.image.load('assets/exit_btn.png').convert_alpha()

run = True

# Buttons
start_Button_game = Button(100, 200, start_img, 0.8)
start_Button_calc = Button(275, 450, start_img, 0.8)
exit_Button = Button(450, 200, exit_img, 0.8)

# Text
text_clac = myfont.render('Rechner', False, (255, 255, 255))
text_game = myfont.render('Spiel zum Zeitvertreib', False, (255, 255, 255))

while run:
    WIN.blit(BG, (0, 0))
    WIN.blit(text_clac, (325, 400))
    WIN.blit(text_game, (50, 150))

    if start_Button_game.draw(WIN):
        print('WORKS')
        os.system("main.py")

    if exit_Button.draw(WIN):
        run = False

    if start_Button_calc.draw(WIN):
        os.system("calc.py")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
