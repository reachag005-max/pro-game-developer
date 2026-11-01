import pygame
import random
import time

pygame.init()
WIDTH = 850
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH,HEIGHT))
ground = pygame.image.load("C:\\Users\\sgarg\\OneDrive\\Desktop\\Python pro game develpoer\\flappy\\ground.png")
Background = pygame.image.load("C:\\Users\\sgarg\\OneDrive\\Desktop\\Python pro game develpoer\\flappy\\background flappy.png")
ground_scroll = 0
scroll_speed = 1
Flying = True
Gameover = False
#groups 
Pipegroup = pygame.sprite.Group()
birdgroup = pygame.sprite.Group()
pipefrequence= 1500
lastpipe = pygame.time.get_ticks() - pipefrequence


class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.image.load("C:\\Users\\sgarg\\OneDrive\\Desktop\\Python pro game develpoer\\flappy\\pipe.png")
        self.rect=self.image.get_rect()
        #1 would be top pipe and -1 would be bottom pipe
        if pos == 1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y]
        elif pos == -1:
            self.rect.topleft = [x,y]

    def update(self):
        self.rect.x -= scroll_speed


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #need to do it outside of for loop 
    screen.blit(Background,(0,-100))
    Pipegroup.draw(screen)
    screen.blit(ground,(ground_scroll,500))


    if not Gameover and Flying:
        timenow = pygame.time.get_ticks()
        if timenow - lastpipe > pipefrequence:
            
            Pipe_H=random.randint(-100,100)
            bottom_p = Pipe(WIDTH,(HEIGHT/2)+Pipe_H,-1)
            top_p = Pipe(WIDTH,(HEIGHT/2)+Pipe_H-150,1)
        



            Pipegroup.add(bottom_p)
            Pipegroup.add(top_p)
            lastpipe = timenow
        Pipegroup.update()

    ground_scroll -= scroll_speed
    print(ground_scroll)

#restting the ground
    if ground_scroll < -50 :
        ground_scroll = 0
    pygame.display.update()

        
