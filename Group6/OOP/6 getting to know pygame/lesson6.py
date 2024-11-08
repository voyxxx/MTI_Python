import pygame
import random
pygame.init()
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

player_width = 50
player_height = 50
obstacle_width = 50
obstacle_height = 50

player_speed = 10
obstacle_speed = 5
score = 0
level = 1

player_x = WIDTH / 2 - player_width / 2
player_y = HEIGHT / 2 - player_height / 2
obstacle_x = WIDTH
obstacle_y = random.randint(top_boundary, bottom_boundary - obstacle_height)

game_over = False

path = './Group6/OOP/6 getting to know pygame/'

sprite_image = pygame.image.load(f'{path}carPlayer.png').convert_alpha()
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
  if keys[pygame.K_a] and player_x > 0:
    player_x -= player_speed
  if keys[pygame.K_d] and player_x < WIDTH - player_width:
    player_x += player_speed
  if keys[pygame.K_w] and player_y > top_boundary:
    player_y -= player_speed
  if keys[pygame.K_s] and player_y < HEIGHT - player_height:
    player_y += player_speed

  obstacle_x -= obstacle_speed

  if obstacle_x + obstacle_width < 0:
    obstacle_x = WIDTH
    obstacle_y = random.randint(top_boundary, bottom_boundary - obstacle_height)
    score += 1
    if (obstacle_speed < 20): obstacle_speed += 1
    if score % 10 == 0:
      level += 1
      # obstacle_speed += 5

  if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width and player_y + player_height > obstacle_y and player_y < obstacle_y + obstacle_height:
      game_over = True

  screen.fill(BLACK)
  pygame.draw.rect(screen, ORANGE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

  screen.blit(sprite_image, (player_x, player_y))

  display_text(f'Score: {score}', 25, 40, 10, WHITE)
  display_text(f'Level: {level}', 25, 40, 40, WHITE)

  pygame.display.update()
  clock.tick(60)

pygame.quit()
