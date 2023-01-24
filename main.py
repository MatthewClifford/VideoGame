import pygame
from sys import exit
from time import sleep
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 600))
background = pygame.image.load("Background.jpg")

# Player
player_surf = pygame.image.load("player_right.png")
player_rect = player_surf.get_rect(bottomright = (425, 530))
player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)

# Enemy #1
enemy1_surf = pygame.image.load("enemy_1_right.png")
enemy1_rect = enemy1_surf.get_rect(bottomleft = (900, 525))
enemy1_surf = pygame.transform.rotozoom(enemy1_surf, 0, 2.5)

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
    enemy1_rect.x -= 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d or pygame.K_a]:
        if keys[pygame.K_d]:
            player_rect.x += 3
        if keys[pygame.K_a]:
            player_rect.x -= 3
            player_surf = pygame.image.load("player_left.png")
            screen.blit(player_surf, player_rect)

# Enemy 1 collision
    """if player_rect.colliderect(enemy1_rect):
        enemy1_rect.x = player_rect.x
        enemy_attacking = True
        while enemy_attacking:
            print("collision")
            sleep(attack_delay)"""

    pygame.display.update()
    clock.tick(60)
