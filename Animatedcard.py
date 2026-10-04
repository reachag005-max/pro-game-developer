import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Animated card")
H1 = pygame.image.load("Halloween1.png")
H1 = pygame.transform.scale(H1,(600,450))
H2 = pygame.image.load("Halloween2.jpg")
H2 = pygame.transform.scale(H2,(600,450))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(("black"))
    screen.blit(H1,(0,150))
    Font = pygame.font.SysFont("Arial",24)
    Text = Font.render("Happy HALLOWEEN!!",True,"orange")
    screen.blit(Text,(200,100))
    pygame.display.update()
    time.sleep(3)

    screen.fill(("black"))


    screen.blit(H2,(0,75))
    pygame.display.update()
    time.sleep(3)
