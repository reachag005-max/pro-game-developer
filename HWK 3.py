import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Shapes & Keyboard Input")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)


current_color = RED

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_color = RED
            elif event.key == pygame.K_2:
                current_color = GREEN
            elif event.key == pygame.K_3:
                current_color = BLUE

  
    screen.fill(WHITE)


    pygame.draw.rect(screen, (200, 200, 200), (100, 300, 200, 150))
    pygame.draw.rect(screen, BLACK, (100, 300, 200, 150), 2)  # Outline
    
    
    pygame.draw.polygon(screen, RED, [(80, 300), (200, 200), (320, 300)])
    pygame.draw.polygon(screen, BLACK, [(80, 300), (200, 200), (320, 300)], 2)  # Outline
    

    pygame.draw.rect(screen, BROWN, (175, 370, 50, 80))
    pygame.draw.rect(screen, BLACK, (175, 370, 50, 80), 2)  # Outline


    pygame.draw.rect(screen, current_color, (500, 300, 150, 150))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()