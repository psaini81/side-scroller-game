import pygame
import sys

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Battle")
CLOCK = pygame.time.Clock()

# Load images (ensure 'player.png' and 'mouse.png' are in the same folder)
PLAYER_IMG = pygame.image.load("player.png")
MOUSE_IMG = pygame.image.load("mouse.png")

# Base Character class
class Character:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health = 100

    def move(self, dx, dy):
        self.x_pos += dx
        self.y_pos += dy

    def state(self):
        return "alive" if self.health > 0 else "dead"

    def draw(self, window, image):
        window.blit(image, (self.x_pos, self.y_pos))

# Player class inherits from Character
class Player(Character):
    def collide(self):
        self.health = max(0, self.health - 20)

# Mouse class inherits from Character
class Mouse(Character):
    def collide(self):
        self.health = max(0, self.health - 10)

def draw_window(player, mouse):
    WIN.fill((255, 255, 255))  # White background
    player.draw(WIN, PLAYER_IMG)
    mouse.draw(WIN, MOUSE_IMG)

    # Draw health text
    font = pygame.font.SysFont(None, 36)
    player_health_text = font.render(f"Player Health: {player.health}", True, (0, 0, 0))
    mouse_health_text = font.render(f"Mouse Health: {mouse.health}", True, (0, 0, 0))
    WIN.blit(player_health_text, (10, 10))
    WIN.blit(mouse_health_text, (10, 50))

    pygame.display.update()

def check_collision(player, mouse):
    player_rect = pygame.Rect(player.x_pos, player.y_pos, PLAYER_IMG.get_width(), PLAYER_IMG.get_height())
    mouse_rect = pygame.Rect(mouse.x_pos, mouse.y_pos, MOUSE_IMG.get_width(), MOUSE_IMG.get_height())
    return player_rect.colliderect(mouse_rect)

def main():
    player = Player(100, 150)
    mouse = Mouse(600, 150)
    speed = 5

    while True:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Key handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-speed, 0)
        if keys[pygame.K_RIGHT]:
            player.move(speed, 0)
        if keys[pygame.K_UP]:
            player.move(0, -speed)
        if keys[pygame.K_DOWN]:
            player.move(0, speed)

        # Collision check
        if check_collision(player, mouse):
            player.collide()
            mouse.collide()

        draw_window(player, mouse)

if __name__ == "__main__":
    main()
