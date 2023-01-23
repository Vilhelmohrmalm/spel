import random


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


class Vapen():
    def __init__(self, v_hp, v_str, v_namn):
        self.v_namn = v_namn
        self.v_hp = v_hp
        self.v_str = v_str


class Karaktärer():
    def __init__(self, p_hp, p_str, p_lvl, p_lvlpoäng, p_namn, vapen):
        self.p_hp = p_hp
        self.p_str = p_str
        self.p_lvl = p_lvl
        self.p_lvlpoäng = p_lvlpoäng
        self.p_namn = p_namn
        self.vapen = vapen


class Monster():
    def __init__(self, m_hp, m_str, m_namn):
        self.m_namn = m_namn
        self.m_hp = m_hp
        self.m_str = m_str

    def __str__(self):
        return f"Du stöter på en {self.m_namn}, den har {self.m_hp} hp och {self.m_str} styrka"


def monstrgenerator_fas1():
    monster = random.randint(1, 2)
    Slime = Monster(health(4, 11), damage(2, 6), "Slime")
    Goblin = Monster(health(3, 7), damage(3, 8), "Goblin")
    if monster == 1:
        monster_stats = (Slime)
        return (monster_stats)
    elif monster == 2:
        monster_stats = (Goblin)
        return (monster_stats)


def monstrgenerator_fas2():
    monster = random.randint(1, 2)
    Lycan = Monster(health(6, 12), damage(4, 9), "Lycan")
    Golem = Monster(health(12, 17), damage(3), "Golem")
    if monster == 1:
        monster_stats = (Lycan)
        return (monster_stats)
    elif monster == 2:
        monster_stats = (Golem)
        return (monster_stats)


def monstrgenerator_fas3():
    monster = random.randint(1, 2)
    Undead = Monster(health(15, 22), damage(4, 5), "Undead")
    Orc = Monster(health(9, 15), damage(6, 10), "Orc")
    if monster == 1:
        monster_stats = (Undead)
        return (monster_stats)
    elif monster == 2:
        monster_stats = (Orc)
        return (monster_stats)


Start = Vapen(0, 0, "en pinne")

Assasin = Karaktärer(5, 10, 0, 0, "assasin", Start)
Barb = Karaktärer(8, 7, 0, 0, "Barb", Start)
Knight = Karaktärer(10, 5, 0, 0, "Knight", Start)
