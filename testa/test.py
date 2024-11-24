print ("hello biatch")
from msvcrt import kbhit
from operator import truediv
import pygame

background_color = (200, 100, 100)

screen = pygame.display.set_mode((600,601))
pygame.display.set_caption("snka game :)")

Borg = pygame.image.load("./ASSets/BoRg.png")
Borgx = 10
Borgy = 10
Borgspeed = 0.05

running = True
while running:

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
        Borgy -= Borgspeed
    if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        Borgx -= Borgspeed
    if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
        Borgy += Borgspeed
    if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        Borgx += Borgspeed
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    screen.fill(background_color)
    screen.blit(Borg,(Borgx,Borgy))
    pygame.display.flip()

