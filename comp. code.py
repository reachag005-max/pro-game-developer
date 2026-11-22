import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Game State Variables
score = 0
high_score = 0
lives = 3
level = 1
combo = 0
game_over = False

# Player Setup
paddle = Rect((350, 530), (110, 20))
base_paddle_width = 110
shield_active = False
powerup_timer = 0

# Dynamic Object Lists
stars = []
obstacles = []
powerups = []

# Spawn Timers
star_timer = 0
obstacle_timer = 0
powerup_timer_spawn = 0

def spawn_star():
    x = random.randint(40, WIDTH - 40)
    speed = random.uniform(3.5, 5.5) + (level * 0.4)
    stars.append({"rect": Rect((x, -30), (25, 25)), "speed": speed})

def spawn_obstacle():
    x = random.randint(40, WIDTH - 40)
    size = random.randint(30, 50)
    speed = random.uniform(4.0, 6.5) + (level * 0.5)
    obstacles.append({"rect": Rect((x, -50), (size, size)), "speed": speed})

def spawn_powerup():
    x = random.randint(40, WIDTH - 40)
    powerups.append({"rect": Rect((x, -30), (25, 25)), "speed": 4.5})

def draw():
    screen.clear()
    screen.fill((20, 22, 38))  # Deep space background

    if not game_over:
        # Draw Shield Aura if active
        if shield_active:
            shield_rect = Rect((paddle.x - 6, paddle.y - 6), (paddle.width + 12, paddle.height + 12))
            screen.draw.rect(shield_rect, (0, 255, 255))

        # Draw Player Paddle
        paddle_color = (0, 255, 200) if shield_active else (50, 205, 50)
        screen.draw.filled_rect(paddle, paddle_color)

        # Draw Stars (Gold)
        for s in stars:
            screen.draw.filled_rect(s["rect"], (255, 215, 0))

        # Draw Obstacles (Crimson)
        for o in obstacles:
            screen.draw.filled_rect(o["rect"], (220, 20, 60))

        # Draw Power-ups (Cyan)
        for p in powerups:
            screen.draw.filled_rect(p["rect"], (0, 255, 255))

        # HUD (Heads-Up Display)
        screen.draw.text(f"Score: {score}", (20, 15), fontsize=32, color="white")
        screen.draw.text(f"High Score: {high_score}", (20, 50), fontsize=24, color="gray")
        screen.draw.text(f"Level: {level}", center=(WIDTH / 2, 25), fontsize=32, color="yellow")
        screen.draw.text(f"Lives: {'♥ ' * lives}", (WIDTH - 160, 15), fontsize=32, color="red")

        if combo > 1:
            screen.draw.text(f"Combo x{combo}!", (WIDTH - 160, 50), fontsize=26, color="gold")

        if powerup_timer > 0:
            screen.draw.text(f"SHIELD: {round(powerup_timer, 1)}s", center=(WIDTH / 2, 55), fontsize=22, color="cyan")

    else:
        screen.draw.text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2 - 60), fontsize=70, color="red")
        screen.draw.text(f"Final Score: {score}  |  Level Reached: {level}", center=(WIDTH / 2, HEIGHT / 2 + 10), fontsize=35, color="white")
        screen.draw.text(f"Best Score: {high_score}", center=(WIDTH / 2, HEIGHT / 2 + 55), fontsize=30, color="gold")
        screen.draw.text("Press 'R' to Play Again", center=(WIDTH / 2, HEIGHT / 2 + 115), fontsize=28, color="cyan")

def update(dt):
    global score, high_score, lives, level, combo, game_over
    global star_timer, obstacle_timer, powerup_timer_spawn, shield_active, powerup_timer

    if game_over:
        if keyboard.r:
            reset_game()
        return

    # Level Progression
    level = (score // 15) + 1

    # Power-up Countdown
    if powerup_timer > 0:
        powerup_timer -= dt
        if powerup_timer <= 0:
            shield_active = False
            paddle.width = base_paddle_width

    # Player Movement (Left/Right or A/D)
    move_speed = 8 + (level * 0.3)
    if (keyboard.left or keyboard.a) and paddle.left > 0:
        paddle.x -= move_speed
    if (keyboard.right or keyboard.d) and paddle.right < WIDTH:
        paddle.x += move_speed

    # Object Spawning Logic
    star_timer += dt
    if star_timer >= max(0.5, 1.3 - (level * 0.08)):
        spawn_star()
        star_timer = 0

    obstacle_timer += dt
    if obstacle_timer >= max(0.4, 1.1 - (level * 0.09)):
        spawn_obstacle()
        obstacle_timer = 0

    powerup_timer_spawn += dt
    if powerup_timer_spawn >= 12.0:  # Spawns every 12 seconds
        spawn_powerup()
        powerup_timer_spawn = 0

    # Update Stars
    for s in stars[:]:
        s["rect"].y += s["speed"]
        if paddle.colliderect(s["rect"]):
            combo += 1
            multiplier = min(combo, 5)  # Max 5x multiplier
            score += 1 * multiplier
            if score > high_score:
                high_score = score
            stars.remove(s)
        elif s["rect"].y > HEIGHT:
            combo = 0  # Reset combo if you miss a star
            stars.remove(s)

    # Update Obstacles
    for o in obstacles[:]:
        o["rect"].y += o["speed"]
        if paddle.colliderect(o["rect"]):
            obstacles.remove(o)
            if shield_active:
                # Shield absorbs the hit!
                shield_active = False
                powerup_timer = 0
                paddle.width = base_paddle_width
            else:
                lives -= 1
                combo = 0
                if lives <= 0:
                    game_over = True
        elif o["rect"].y > HEIGHT:
            obstacles.remove(o)

    # Update Power-ups
    for p in powerups[:]:
        p["rect"].y += p["speed"]
        if paddle.colliderect(p["rect"]):
            shield_active = True
            powerup_timer = 6.0
            paddle.width = int(base_paddle_width * 1.5)
            powerups.remove(p)
        elif p["rect"].y > HEIGHT:
            powerups.remove(p)

def reset_game():
    global score, lives, level, combo, game_over
    global stars, obstacles, powerups, shield_active, powerup_timer
    score = 0
    lives = 3
    level = 1
    combo = 0
    game_over = False
    shield_active = False
    powerup_timer = 0
    paddle.width = base_paddle_width
    paddle.x = 350
    stars.clear()
    obstacles.clear()
    powerups.clear()

pgzrun.go()