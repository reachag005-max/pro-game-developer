import pygame
from pygame.locals import *

pygame.init()
width= 600
height = 400
screen = pygame.display.set_mode((width,height))


class Ball():
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color
        self.pos = 300,200
        pygame.draw.circle(screen,self.color,self.pos,self.radius,100)
    def growball(self,sizeinc):
        #self.sizeinc = sizeinc + radius
        
        self.radius = self.radius + sizeinc
        pygame.draw.circle(screen,self.color,self.pos,self.radius,100)
    def reducesize(self,reducesize):
        
        self.raadius = self.radius - reducesize
        pygame.draw.circle(screen,self.color,self.pos,self.radius,100)
        

Ball1 = Ball(50,"Green")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Ball1.growball(20)
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                screen.fill((0,0,0))
                Ball1.reducesize(40)
    pygame.display.update()