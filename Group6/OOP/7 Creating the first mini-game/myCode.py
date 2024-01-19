import pygame
import random
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 100, 0)
PURPLE = (255, 0, 255)

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Убеги от препятствий')

clock = pygame.time.Clock()

top_boundary = 0
bottom_boundary = HEIGHT

player_width = 50
player_height = 50
obstacle_width = 50
obstacle_height = 50

player_speed = 10
obstacle_speed = 5
score = 0
level = 1

#начальные позиции для первого и второго игрока
player1_x = WIDTH
player1_y = HEIGHT / 2 - player_height / 2

player2_x = WIDTH - 300  - player_width
player2_y = HEIGHT / 2 - player_height / 2

obstacle_x = WIDTH
obstacle_y = random.randint(top_boundary, bottom_boundary - obstacle_height)

game_over = False

path = './Group6/OOP/7 Creating the first mini-game/'

sprite_image = pygame.image.load(f'{path}carPlayer.png').convert_alpha()
sprite_image2 = pygame.image.load(f'{path}jeep.png').convert_alpha()
# sprite_image = pygame.image.load('carPlayer').convert_alpha()

def display_text(text, font_size, x, y, color):
  font = pygame.font.Font(None, font_size)
  text_surface = font.render(text, True, color)
  screen.blit(text_surface, (x, y))

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True

  keys = pygame.key.get_pressed()
  if keys[pygame.K_a] and player1_y > top_boundary:
    player1_y -= player_speed
  if keys[pygame.K_d] and player1_y < bottom_boundary - player_height:
    player1_y += player_speed

  # управление вторым игроком
  if keys[pygame.K_UP] and player2_y > top_boundary:
    player2_y -= player_speed
  if keys[pygame.K_DOWN] and player2_y < bottom_boundary - player_height:
    player2_y += player_speed
    
  obstacle_x -= obstacle_speed

  if obstacle_x + obstacle_width < 0:
    obstacle_x = WIDTH
    obstacle_y = random.randint(top_boundary, bottom_boundary - obstacle_height)
    score += 1
    if (obstacle_speed < 20): obstacle_speed += 1
    if score % 10 == 0:
      level += 1
      # obstacle_speed += 5

   
    if player1_x + player_width > obstacle_x and player1_x < obstacle_x + obstacle_width and player1_y + player_height > obstacle_y and player1_y < obstacle_y + obstacle_height:
        game_over = True
    if player2_x + player_width > obstacle_x and player2_x < obstacle_x + obstacle_width and player2_y + player_height > obstacle_y and player2_y < obstacle_y + obstacle_height:
        game_over = True

  screen.fill(BLACK)
  pygame.draw.rect(screen, ORANGE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

  screen.blit(sprite_image, (player1_x, player1_y))
  screen.blit(sprite_image2, (player2_x, player2_y))

  display_text(f'Score: {score}', 25, 40, 10, WHITE)
  display_text(f'Level: {level}', 25, 40, 40, WHITE)

  pygame.display.update()
  clock.tick(60)

pygame.quit()
