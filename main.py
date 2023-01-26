import pygame
from sys import exit
from time import sleep
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 535))
health_font = pygame.font.Font('Pixeltype.ttf', 50)
background = pygame.image.load("background1.jpg")
background = pygame.transform.rotozoom(background, 0, 2)

# Player
player_surf = pygame.image.load("player_sprites/player_right.png").convert_alpha()
player_rect = player_surf.get_rect(bottomright = (575, 470))
player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5).convert_alpha()
player_gravity = 0
player_health = 50
health_display = health_font.render(f"Health: {player_health} ", False, (0, 0, 0))
# Enemy #1
enemy1_surf = pygame.image.load("enemy1sprites/enemy1_right.png").convert_alpha()
enemy1_rect = enemy1_surf.get_rect(bottomleft = (1100, 462))
enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5).convert_alpha()
enemy1_health = 10
enemy1_kills = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(player_surf, player_rect)
    screen.blit(enemy1_surf, enemy1_rect)
    screen.blit(health_display, (550, 75))

    # Player Movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_surf = pygame.image.load("player_sprites/player_left.png")
            player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)
            player_rect.x -= 4
        if event.key == pygame.K_RIGHT:
            player_surf = pygame.image.load("player_sprites/player_right.png")
            player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)
            player_rect.x += 4
        if player_rect.x >= 1075:
            player_rect.x = 1075
        elif player_rect.x <= 0:
            player_rect.x = 0

    if enemy1_rect.x == player_rect.x:
        player_health -= 0.001
        print(player_health)


        """if enemy1_rect.x == player_rect.x and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                enemy1_health -= 2

        if enemy1_health <= 0:
            enemy1_surf.kill(enemy1_surf)"""

        if int(player_health) == 0:
            exit()

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
