import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Catch the Apple")
clock = pygame.time.Clock()

snake= pygame.image.load("snake.png")
snake = pygame.transform.scale(snake, (50, 50))

Apple = pygame.image.load("apple.png")
Apple = pygame.transform.scale(Apple, (40, 40))

x = 400
y = 300
size = 50
speed = 6

target_x = random.randint(50, 730)
target_y = random.randint(50, 530)
target_size = 40

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    player_rect = pygame.Rect(x, y, size, size)
    target_rect = pygame.Rect(target_x, target_y, target_size, target_size)

    if player_rect.colliderect(target_rect):
        score += 1
        target_x = random.randint(50, 730)
        target_y = random.randint(50, 530)

    screen.fill((30, 30, 30))
    screen.blit(snake, (x, y))
    screen.blit(Apple, (target_x, target_y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()