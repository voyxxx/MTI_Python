import pygame
import random

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 100, 0)
PUR = (255, 0, 255)

FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My game')

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

# Начальный позиции двух игроков
player1_x = 100
player1_y = HEIGHT/2 - player_height/2

player2_x = WIDTH - 100 - player_width
player2_y = HEIGHT/2 - player_height/2
# конец блока кода для начальных позиций двух игроков

# player_x = WIDTH/2 - player_width/2
# player_y = HEIGHT/2 - player_height/2
obstacle_x = WIDTH
obstacle_y = random.randint(top_boundary, bottom_boundary - obstacle_height)

game_over = False

def display_text(text, font_size, x, y, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > top_boundary:
        player1_y -= player_speed
    if keys[pygame.K_s] and player1_y < bottom_boundary - player_height:
        player1_y += player_speed
    # управление для второго игрока
    if keys[pygame.K_UP] and player2_y > top_boundary:
        player2_y -= player_speed
    if keys[pygame.K_DOWN] and player2_y < bottom_boundary - player_height:
        player2_y += player_speed

    obstacle_x -= obstacle_speed

    if obstacle_x + obstacle_width < 0:
        obstacle_x = WIDTH
        obstacle_y = random.randint(top_boundary, bottom_boundary - obstacle_height)
        score += 1
        if score % 10 == 0:
            level += 1
            obstacle_speed += 3

    if player1_x + player_width > obstacle_x and player1_x < obstacle_x + obstacle_width and player1_y + player_height > obstacle_y and player1_y < obstacle_y + obstacle_height:
        game_over = True
    if player2_x + player_width > obstacle_x and player2_x < obstacle_x + obstacle_width and player2_y + player_height > obstacle_y and player2_y < obstacle_y + obstacle_height:
        game_over = True

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (player1_x, player1_y, player_width, player_height))
    pygame.draw.rect(screen, PUR, (player2_x, player2_y, player_width, player_height))
    pygame.draw.rect(screen, WHITE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    display_text(f'Score: {score}', 25, 10, 10, WHITE)
    display_text(f'Level: {level}', 25, 10, 40, WHITE)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()