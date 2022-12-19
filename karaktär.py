from text_animering import *
import random
from valfunktioner import *
from fight import *


def health(a, b):
    health = []
    for i in range(a, b+1):
        health.append(i)
    return (random.choice(health))


def damage(a, b):
    damage = []
    for i in range(a, b+1):
        damage.append(i)
    return (random.choice(damage))




class Karaktärer():
    def __init__(self, p_hp, p_str, p_namn):
        self.p_hp = p_hp
        self.p_str = p_str
        self.p_namn = p_namn
        self.vapen_lista = []


class Monster():
    def __init__(self, m_hp, m_str, m_namn):
        self.m_namn = m_namn
        self.m_hp = m_hp
        self.m_str = m_str

    def __str__(self):
        return f"Du stöter på en {self.m_namn}, den har {self.m_hp} hp och {self.m_str} styrka"

def monstrgenerator():
    monster=random.randint(1,2)
    if monster == 1:
        monster_stats=(Slime)
        return(monster_stats)
    elif monster == 2:
        monster_stats=(Goblin)
        return(monster_stats)


Slime = Monster(health(4, 11), damage(1, 6), "Slime")
Goblin = Monster(health(3, 7), damage(3, 8), "Goblin")

Assasin = Karaktärer(5, 10, "assasin")
Barb = Karaktärer(8, 7, "Barb")
Knight = Karaktärer(10, 5, "Knight")
