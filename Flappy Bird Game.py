import pygame

pygame.init()
WIDTH = 850
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH,HEIGHT))
ground = pygame.image.load("C:\\Users\\sgarg\\OneDrive\\Desktop\\Python pro game develpoer\\flappy\\ground.png")
Background = pygame.image.load("C:\\Users\\sgarg\\OneDrive\\Desktop\\Python pro game develpoer\\flappy\\background flappy.png")
ground_scroll = 0
scroll_speed = 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #need to do it outside of for loop 
    screen.blit(Background,(0,-100))
    screen.blit(ground,(ground_scroll,500))

    ground_scroll -= scroll_speed
    print(ground_scroll)

   #restting the ground
    if ground_scroll < -50 :
        ground_scroll = 0
    pygame.display.update()

        
