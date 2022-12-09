import random
import pygame

# storleken på labyrinten
width = 10
height = 10

# en lista för att lagra kartan
map = []

# skapa en tom karta
for y in range(height):
    row = []
    for x in range(width):
        row.append('.')
    map.append(row)

# slumpmässigt placera väggar och gångar i labyrinten
for y in range(1, height-1):
    for x in range(1, width-1):
        if random.random() > 0.5:
            map[y][x] = '#'
        else:
            map[y][x] = '.'

# placera spelaren i en slumpmässig position
player_x = random.randint(1, width-2)
player_y = random.randint(1, height-2)
map[player_y][player_x] = '@'

# skapa fönstret med Pygame
pygame.init()
screen = pygame.display.set_mode((width*32, height*32))

# ladda bilder med Pygame
wall_img = pygame.image.load('wall.png')
floor_img = pygame.image.load('floor.png')
player_img = pygame.image.load('player.png')

# rita kartan med bilder i Pygame
for y in range(height):
    for x in range(width):
        if map[y][x] == '#':
            screen.blit(wall_img, (x*32, y*32))
        elif map[y][x] == '.':
            screen.blit(floor_img, (x*32, y*32))
        elif map[y][x] == '@':
            screen.blit(player_img, (x*32, y*32))

# uppdatera skärmen med Pygame
pygame.display.flip()

# håll fönstret öppet tills spelaren stänger det
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
