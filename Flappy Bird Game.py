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
Pipefrequency= 1575
lastpipe = pygame.time.get_ticks() - Pipefrequency




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
class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.flappy = []
        self.index = 0
        self.count = 0
        for i in range (1,4):
            self.flappy1 = pygame.image.load(f"C:\\Users\\sgarg\\OneDrive\\Desktop\\Python pro game develpoer\\flappy\\Flappy {i}.png")
            self.flappy.append(self.flappy1)
        self.image = self.flappy[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.click = False
        self.velocity = 0
    def update(self):
        if Flying == True:
            self.velocity += 0.1 
            print(self.velocity)
            if self.velocity > 20:
                self.velocity = 1

            if self.rect.bottom < 500:
                self.rect.y += self.velocity
        if Gameover == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.velocity -= 15
                 





#creating object bird
Flappybird = Bird(100,HEIGHT//2)
birdgroup.add(Flappybird)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #need to do it outside of for loop 
    screen.blit(Background,(0,-100))
    Pipegroup.draw(screen)
    screen.blit(ground,(ground_scroll,500))

    birdgroup.draw(screen)
    birdgroup.update()

    if not Gameover and Flying:
        timenow = pygame.time.get_ticks()
        if timenow - lastpipe > Pipefrequency:
            
            Pipe_H=random.randint(-100,100)
            bottom_p = Pipe(WIDTH,(HEIGHT/2)+Pipe_H,-1)
            top_p = Pipe(WIDTH,(HEIGHT/2)+Pipe_H-150,1)
        



            Pipegroup.add(bottom_p)
            Pipegroup.add(top_p)
            lastpipe = timenow
        Pipegroup.update()

    ground_scroll -= scroll_speed


#restting the ground
    if ground_scroll < -50 :
        ground_scroll = 0
    pygame.display.update()