import pgzrun

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.v = 0  
        self.g = 0.5  

    def update(self):
        if self.y + self.radius < HEIGHT:
            self.v += self.g
            self.y += self.v

            if self.y + self.radius >= HEIGHT:
                self.y = HEIGHT - self.radius
                self.v = 0

    def reset(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.v = 0

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, (50, 150, 255))

ball = Ball(x=WIDTH // 2, y=100, radius=25)

def update():
    ball.update()

def draw():
    screen.fill((255, 255, 255))
    ball.draw()

def on_key_down(key):
    
    if key == keys.R:
        ball.reset(WIDTH // 2, 100)

pgzrun.go()