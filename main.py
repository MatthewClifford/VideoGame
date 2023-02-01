# Video Game
# 1.30.23

# Import Libraries here...
import random
import pygame
from sys import exit
import random
from random import randrange
from time import sleep

pygame.init()
clock = pygame.time.Clock()

# Background Music
bg_music = pygame.mixer.Sound('music_zapsplat_astro_race.mp3')
bg_music.play(loops=-1)
bg_music.set_volume(0.3)


# Screen/background
screen = pygame.display.set_mode((1200, 535))
background = pygame.image.load("background1.jpg")
background = pygame.transform.rotozoom(background, 0, 2)

# Player
player_surf = pygame.image.load("player_sprites/player_right.png").convert_alpha()
player_rect = player_surf.get_rect(bottomright = (575, 470))
player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5).convert_alpha()

# Health...
health = 50
health_font = pygame.font.Font('Pixeltype.ttf', 50)
health_display = health_font.render(f"Health {health}", True, (0, 0, 0))

# Enemy #1
enemy1_hp = 10
enemyx_position = randrange(1200, 1500)
enemy1_surf = pygame.image.load("enemy1sprites/enemy1_right.png").convert_alpha()
enemy1_rect = enemy1_surf.get_rect(bottomleft = ((enemyx_position), 462))
enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5).convert_alpha()

# Player Movement function
def player_movement():
    global player_surf
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_surf = pygame.image.load("player_sprites/player_left.png")
            player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)
            player_rect.x -= 4

        if event.key == pygame.K_RIGHT:
            player_surf = pygame.image.load("player_sprites/player_right.png")
            player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)
            player_rect.x += 4

def enemy1_follow_collision():
    global health, enemy1_surf, health_display
    if player_rect.x > enemy1_rect.x:
        enemy1_surf = pygame.image.load("enemy1sprites/enemy1_right.png")
        enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5)
        enemy1_rect.x += 2

    if player_rect.x < enemy1_rect.x:
        enemy1_surf = pygame.image.load("enemy1sprites/enemy1_left.png")
        enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5)
        enemy1_rect.x -= 2

    # Collision with enemy
    if player_rect.x == enemy1_rect.x:
        enemy1_surf = pygame.image.load("enemy1sprites/enemy1_left.png")
        enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5)
        health -= 0.03
        print(int(health))
        health_display = health_font.render(f"Health {int(health)}", True, (0, 0, 0))


# Game Loop
level_one = True
while level_one:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw Images on the screen
    screen.blit(background, (0, 0))
    screen.blit(enemy1_surf, enemy1_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(health_display, (550, 75))

    # Player Movement
    player_movement()

    # Enemy 1 AI
    enemy1_follow_collision()

    # Window Edge
    if player_rect.x >= 1075:
        player_rect.x = 1075
    elif player_rect.x <= 0:
        player_rect.x = 0

    # Player Attacking
    if player_rect.x >= enemy1_rect.x + 200:
        print("test")

    elif player_rect.x <= enemy1_rect.x - 200:
        print('test')

    # Attacking
    else:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                enemy1_hp -= 0.3
                print("EnemyHP:", int(enemy1_hp))
                player_surf = pygame.image.load("player_sprites/player_attack.png")
                player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)

    if enemy1_hp <= 0:
        print("Kill")
        enemy1_hp += 10
        enemy1_follow_collision()
        enemy1_rect.x = randrange(1200, 1500)

    pygame.display.update()
    clock.tick(60)

