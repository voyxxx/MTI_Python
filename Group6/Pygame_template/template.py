import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 100, 0)

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Убеги от препятствий')

clock = pygame.time.Clock()

top_boundary = 0
bottom_boundary = HEIGHT

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True

  pygame.display.update()
  clock.tick(60)

pygame.quit()
