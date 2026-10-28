import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 120, 255)

clock = pygame.time.Clock()

player_width = 50
player_height = 40
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - 70
player_speed = 5

bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

enemy_width = 40
enemy_height = 40
enemy_speed = 3
enemies = []

SPAWN_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY, 1000)

while True:
  screen.fill(BLACK)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      raise SystemExit

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bullet_x = player_x + player_width // 2 - bullet_width // 2
        bullet_y = player_y
        bullets.append([bullet_x, bullet_y])

    if event.type == SPAWN_ENEMY:
      enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
      enemy_y = -enemy_height
      enemies.append([enemy_x, enemy_y])

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and player_x > 0:
    player_x -= player_speed
  if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
    player_x += player_speed

  for bullet in bullets[:]:
    bullet[1] -= bullet_speed
    if bullet[1] < 0:
      bullets.remove(bullet)

  for enemy in enemies[:]:
    enemy[1] += enemy_speed
    if enemy[1] > SCREEN_HEIGHT:
      enemies.remove(enemy)

  for bullet in bullets[:]:
    bullet_rect = pygame.Rect(
        bullet[0], bullet[1], bullet_width, bullet_height
    )
    for enemy in enemies[:]:
      enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height)
      if bullet_rect.colliderect(enemy_rect):
        if bullet in bullets:
          bullets.remove(bullet)
        if enemy in enemies:
          enemies.remove(enemy)
        break

  pygame.draw.rect(
      screen,
      BLUE,
      (player_x, player_y, player_width, player_height),
  )

  for bullet in bullets:
    pygame.draw.rect(
        screen,
        WHITE,
        (bullet[0], bullet[1], bullet_width, bullet_height),
    )

  for enemy in enemies:
    pygame.draw.rect(
        screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height)
    )

  pygame.display.flip()
  clock.tick(60)