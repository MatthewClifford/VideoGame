import pygame
from sys import exit
from time import sleep
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200, 560))
background = pygame.image.load("background.jpg")
background = pygame.transform.rotozoom(background, 0, 0.2)

# Player
player_surf = pygame.image.load("player_sprites/player_right.png")
player_rect = player_surf.get_rect(bottomright = (425, 495))
player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)
player_gravity = 0

# Enemy #1
enemy1_surf = pygame.image.load("enemy1sprites/enemy1_right.png")
enemy1_rect = enemy1_surf.get_rect(bottomleft = (900, 485))
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
# Player Jump
        """if event.key == pygame.K_UP and player_rect.bottom >= 495:
            player_rect.y -= player_gravity"""




# Enemy 1 collision
    #if enemy1_rect.colliderect(player_rect):
        #enemy1_rect.x = player_rect.x
        #print("collision")

    #player_surf = pygame.image.load("player_sprites/player_jump.png")
    #player_surf = pygame.transform.rotozoom(player_surf, 0, 2.5)

    if player_rect.x != enemy1_rect.x:
        if player_rect.x > enemy1_rect.x:
            enemy1_rect.x += 1
        elif player_rect.x < enemy1_rect.x:
            enemy1_rect.x -= 1

    pygame.display.update()
    clock.tick(60)