import random

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

# skriv ut kartan
for row in map:
    print(''.join(row))
