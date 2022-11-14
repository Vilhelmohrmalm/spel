
import random

def m_health(a,b):
    health=[]
    for i in range(a,b+1):
        health.append(i)
    return(random.choice(health))

def m_damage(a,b):
    damage=[]
    for i in range(a,b+1):
        damage.append(i)
    return(random.choice(damage))

class karaktär():
    def __init__(self, p_hp, p_str, p_namn):
        self.p_hp=p_hp
        self.p_str=p_str
        self.p_namn=p_namn




class monster():
    def __init__(self, m_hp, m_str, m_namn):
        self.namn =m_namn
        self.m_hp=m_hp
        self.m_str=m_str

    def __str__(self):
        return f"Du stöter på en {self.m_namn}, den har {self.m_hp} hp och {self.m_str} styrka"


slime= monster(m_health(4,11), m_damage(1,6), "slime")
goblin= monster(m_health(3,7), m_damage(3,8), "goblin")

assasin= karaktär(5, 10, "assasin")
barb= karaktär(8, 7, "barb")
knight= karaktär(10, 5, "knight")

