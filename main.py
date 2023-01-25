import pygame
from sys import exit
from time import sleep
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 560))
health_font = pygame.font.Font('Pixeltype.ttf', 50)
background = pygame.image.load("background.jpg")
background = pygame.transform.rotozoom(background, 0, 0.2)

# Player
player_surf = pygame.image.load("player_sprites/player_right.png").convert_alpha()
player_rect = player_surf.get_rect(bottomright = (575, 495))
player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5).convert_alpha()
player_gravity = 0
player_health = 50
health_display = health_font.render(f"Health: {player_health} ", False, (0, 0, 0))
# Enemy #1
enemy1_surf = pygame.image.load("enemy1sprites/enemy1_right.png").convert_alpha()
enemy1_rect = enemy1_surf.get_rect(bottomleft = (1100, 485))
enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5).convert_alpha()

# Delay between enemy attack
attack_delay = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(player_surf, player_rect)
    screen.blit(enemy1_surf, enemy1_rect)
    screen.blit(health_display, (550,50))
# Player Movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_surf = pygame.image.load("player_sprites/player_left.png")
            player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)
            player_rect.x -= 3.5
        if event.key == pygame.K_RIGHT:
            player_surf = pygame.image.load("player_sprites/player_right.png")
            player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)
            player_rect.x += 3.5
        if player_rect.x >= 1075:
            player_rect.x = 1075
        elif player_rect.x <= 0:
            player_rect.x = 0
# Player Jump

    # Enemy 1 collision
    if enemy1_rect.x == player_rect.x:
        player_health -= 0.05

    if int(player_health) == 0:
        exit()

    #player_surf = pygame.image.load("player_sprites/player_jump.png")
    #player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)
# Enemy 1 AI
    if player_rect.x != enemy1_rect.x:
        if player_rect.x > enemy1_rect.x:
            enemy1_surf = pygame.image.load("enemy1sprites/enemy1_right.png")
            enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5)
            enemy1_rect.x += 1
        elif player_rect.x < enemy1_rect.x:
            enemy1_surf = pygame.image.load("enemy1sprites/enemy1_left.png")
            enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5)
            enemy1_rect.x -= 1

    pygame.display.update()
    clock.tick(60)