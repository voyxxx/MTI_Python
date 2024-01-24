import pygame
import random

pygame.init()
pygame.mixer.init()

HEIGHT = 600
BACKGROUND_COLOR = (0, 255, 204)
RECT_COLOR = (255, 255, 255)
ODD_RECT_COLOR = (204, 255, 255)
APPLE_COLOR = (255, 0, 0)
SIZE_RECT = 20
COUNT_RECT = 20
RETURN = 1
WIDTH = SIZE_RECT * COUNT_RECT + 2 * SIZE_RECT + RETURN * (COUNT_RECT - 1)

HEADER_HEIGHT = 70
HEADER_COLOR = (0, 255, 160) 
COLOR_SNAKE = (0, 102, 0)

isGameOver = False
# isAppleEaten = False

path = './Group6/OOP/8 pyGame part 1/'
pygame.mixer.music.load(f'{path}I\'m Alone.mp3')
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0)


app = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry Snake')

def draw_rect(color, row, column):
  x = SIZE_RECT + column * SIZE_RECT + RETURN * column
  y = HEADER_HEIGHT + SIZE_RECT + row * SIZE_RECT + RETURN * row
  pygame.draw.rect(app, color, [x, y, SIZE_RECT, SIZE_RECT])

def checkGameOver(head):
  if (not head.inside()): 
    isGameOver = True 
    return True

class Snake:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # def __str__(self):
  #   return f'({self.x}, {self.y})'

  # def __repr__(self):
  #   kvps = [f"{k}={v}" for k, v in vars(self).items()]
  #   return f"{type(self).__name__}({', '.join(kvps)})"

  def inside(self):
    return 0 <= self.x < COUNT_RECT and 0 <= self.y < COUNT_RECT

snake_rect = [Snake(9, 9)]
food = Snake(4, 5)
x_row = 0
y_col = 1

class Apple:
  def __init__(self):
    self.isEaten = True
    self.createApple()

  def createApple(self):
    self.x = random.randint(0, COUNT_RECT - 1)
    self.y = random.randint(0, COUNT_RECT - 1)

    for rect in snake_rect:
      if (rect.x == self.x and rect.y == self.y):
        self.createApple()
        break

  def drawApple(self):
    if self.isEaten:
      draw_rect(APPLE_COLOR, self.x, self.y)
      self.isEaten = False
    

apple = Apple()

time = pygame.time.Clock()

while not isGameOver:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isGameOver = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        isGameOver = True
        break
      # if event.key == pygame.K_UP and x_row != 1:
      if event.key == pygame.K_UP and y_col != 0:
        x_row = -1
        y_col = 0
      # if event.key == pygame.K_DOWN and x_row != -1:
      if event.key == pygame.K_DOWN and y_col != 0:
        x_row = 1
        y_col = 0
      # if event.key == pygame.K_LEFT and y_col != 1:
      if event.key == pygame.K_LEFT and x_row != 0:
        x_row = 0
        y_col = -1
      # if event.key == pygame.K_RIGHT and y_col != -1:
      if event.key == pygame.K_RIGHT and x_row != 0:
        x_row = 0
        y_col = 1

  # refill window
  app.fill(BACKGROUND_COLOR)

  # it draw the score board
  pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIDTH, HEADER_HEIGHT])

  # it draw the game field
  for column in range(COUNT_RECT):
    for row in range(COUNT_RECT):
      color = RECT_COLOR if (column + row) % 2 == 0 else ODD_RECT_COLOR
      draw_rect(color, row, column)

  # it draw the snake
  head = snake_rect[-1]
  new_head = Snake(head.x + x_row, head.y + y_col)
  snake_rect.append(new_head)
  snake_rect.pop(0)

  # check for game over
  if (checkGameOver(new_head)): break

  if (new_head.x == apple.x and new_head.y == apple.y):
    apple.createApple()

  draw_rect(APPLE_COLOR, food.x, food.y)  
  
  for rect in snake_rect:
    draw_rect(COLOR_SNAKE, rect.x, rect.y)  

  # apple.drawApple()
  
  pygame.display.update()
  time.tick(2)


pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()