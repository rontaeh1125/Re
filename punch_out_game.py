import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load Assets (Replace with your own images)
player_image = pygame.Surface((50, 50))  # Placeholder for player's sprite
player_image.fill((0, 255, 0))

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT - 60))
        self.health = 100

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        self.rect.x = max(0, min(WIDTH - 50, self.rect.x))

# Define Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image.copy()  # Placeholder for enemy's sprite
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), 50))

    def update(self):
        # Basic AI for the enemy
        if self.rect.x < WIDTH/2:
            self.rect.x += random.randint(1, 3)
        else:
            self.rect.x -= random.randint(1, 3)
        self.rect.y += 1
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(50, WIDTH - 50)

# Create Sprite Groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Create enemies
enemies = pygame.sprite.Group()
for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Main Game Loop
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Punch-Out Inspired Game')
clock = pygame.time.Clock()  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()  
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()