import pygame
import random

pygame.init()

HEIGHT = 600
BACKGROUND_COLOR = (0, 255, 204)
RECT_COLOR = (255, 255, 255)
ODD_RECT_COLOR = (204, 255, 255)
SIZE_RECT = 20
COUNT_RECT = 20
RETURN = 1
WIDTH = SIZE_RECT * COUNT_RECT + 2 * SIZE_RECT + RETURN * COUNT_RECT

HEADER_HEIGHT = 70
HEADER_COLOR = (0, 255, 160) 

path = './Group6/OOP/8 pyGame part 1/lesson8.py'

app = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry Snake')

isGameOver = False

while not isGameOver:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isGameOver = True

  app.fill(BACKGROUND_COLOR)

  pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIDTH, HEADER_HEIGHT])
  
  for column in range(COUNT_RECT):
    for row in range(COUNT_RECT):
      x = SIZE_RECT + column * SIZE_RECT + RETURN * (column + 1)
      y = HEADER_HEIGHT + SIZE_RECT + row * SIZE_RECT + RETURN * (row + 1)
      
      color = RECT_COLOR if (column + row) % 2 == 0 else ODD_RECT_COLOR

      pygame.draw.rect(app, color, [x, y, SIZE_RECT, SIZE_RECT])
  
  pygame.draw.rect(app, RECT_COLOR, [SIZE_RECT, HEADER_HEIGHT + SIZE_RECT, SIZE_RECT, SIZE_RECT])
  pygame.display.update()

  