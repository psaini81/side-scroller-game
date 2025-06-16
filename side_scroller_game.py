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


        
