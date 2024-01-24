
import pygame
import random

pygame.init()
pygame.mixer.init()

HEIGHT = 600
BACKGROUND_COLOR = (0, 255, 204)
RECT_COLOR = (255, 255, 255)
ODD_RECT_COLOR = (204, 255, 255)
APPLE_COLOR = (255, 0, 0)
TEXT_COLOR = (0, 0, 0)
SIZE_RECT = 20
COUNT_RECT = 20
RETURN = 1
WIDTH = SIZE_RECT * COUNT_RECT + 2 * SIZE_RECT + RETURN * (COUNT_RECT - 1)

HEADER_HEIGHT = 70
HEADER_COLOR = (0, 255, 160) 
COLOR_SNAKE = (0, 102, 0)

isGameOver = False
isGameStarted = False
speed = 5

# path = './Group6/OOP/8 pyGame part 1/'
path = './'
pygame.mixer.music.load(f'{path}I\'m Alone.mp3')
pygame.mixer.music.play(-1)


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

  def __eq__(self, other):
    return isinstance(other, Snake) and (self.x, self.y) == (other.x, other.y)

  # def __str__(self):
  #   return f'({self.x}, {self.y})'

  # def __repr__(self):
  #   kvps = [f"{k}={v}" for k, v in vars(self).items()]
  #   return f"{type(self).__name__}({', '.join(kvps)})"

  def inside(self):
    return 0 <= self.x < COUNT_RECT and 0 <= self.y < COUNT_RECT

def randomFoodPlace():
  x = random.randint(0, COUNT_RECT - 1)
  y = random.randint(0, COUNT_RECT - 1)
  food_block = Snake(x, y)
  while food_block in snake_rect:
    food_block.x = random.randint(0, COUNT_RECT - 1)
    food_block.y = random.randint(0, COUNT_RECT - 1)
  return food_block

snake_rect = [Snake(9, 9)]
food = Snake(4, 5)
x_row = 0
y_col = 1
result = 0

time = pygame.time.Clock()
text = pygame.font.SysFont('courier', 30, True)

while not isGameOver:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      isGameOver = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        isGameOver = True
        break
      if not isGameStarted:
        isGameStarted = True
      elif event.key == pygame.K_UP and y_col != 0:
        x_row = -1
        y_col = 0
      elif event.key == pygame.K_DOWN and y_col != 0:
        x_row = 1
        y_col = 0
      elif event.key == pygame.K_LEFT and x_row != 0:
        x_row = 0
        y_col = -1
      elif event.key == pygame.K_RIGHT and x_row != 0:
        x_row = 0
        y_col = 1

  # refill window
  app.fill(BACKGROUND_COLOR)

  if not isGameStarted:
    text_menu = text.render('For start press key', 4, TEXT_COLOR)
    app.blit(text_menu, (SIZE_RECT * 3, HEIGHT // 2))
  else:
    pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIDTH, HEADER_HEIGHT])

    # it draw the score board
    pygame.draw.rect(app, HEADER_COLOR, [0, 0, WIDTH, HEADER_HEIGHT])

    # it draw the game field
    for column in range(COUNT_RECT):
      for row in range(COUNT_RECT):
        color = RECT_COLOR if (column + row) % 2 == 0 else ODD_RECT_COLOR
        draw_rect(color, row, column)

    # it calculate the snake
    head = snake_rect[-1]
    new_head = Snake(head.x + x_row, head.y + y_col)
    if food == new_head:
      result += 1
      snake_rect.append(food)
      food = randomFoodPlace()
    else:
      snake_rect.append(new_head)
      snake_rect.pop(0)

    # check for game over
    if (checkGameOver(new_head)): break

    draw_rect(APPLE_COLOR, food.x, food.y)  
    
    for rect in snake_rect:
      draw_rect(COLOR_SNAKE, rect.x, rect.y)  

    text_result = text.render(f'Result: {result}', 0, TEXT_COLOR)
    app.blit(text_result, (SIZE_RECT, SIZE_RECT))
  
  pygame.display.update()
  time.tick(speed)


pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()