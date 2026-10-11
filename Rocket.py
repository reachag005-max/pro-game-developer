import pygame
from pygame.locals import * 
import time

pygame.init()

screen = pygame.display.set_mode((600,600))
Rocket = pygame.image.load("Rocket.png")
Background = pygame.image.load("background.jpg")


Rocket_x = 300
Rocket_y = 250
#[up,left,down,right]
Movement = [False,False,False,False]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_w:
                Movement[0]=True
            elif event.key == K_a:
                Movement[1]=True
            
        elif event.type == pygame.KEYUP:
            if event.key == K_w:
                Movement[0]=False
    if Movement[0]:
        Rocket_y -=10
    pygame.display.update()
    screen.blit(Background,(0,0))    
    screen.blit(Rocket,(Rocket_x,Rocket_y))
    Rocket_y +=1
    time.sleep(0.5) 
    pygame.display.update()