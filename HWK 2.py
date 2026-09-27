import pgzrun
import random

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = random.choice([-5, -4, -3, 3, 4, 5])
        self.vy = random.choice([-5, -4, -3, 3, 4, 5])
       
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.vx *= -1


        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.vy *= -1

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

balls = [
    Ball(
        x=random.randint(50, WIDTH - 50),
        y=random.randint(50, HEIGHT - 50),
        radius=20
    ) for _ in range(5)
]

def update():
    for ball in balls:
        ball.update()

def draw():
    screen.fill((255, 255, 255))
    for ball in balls:
        ball.draw()

pgzrun.go()