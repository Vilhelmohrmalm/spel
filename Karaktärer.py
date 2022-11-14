import random

class karaktär():
    def _init_(self, p_hp, p_str):
        self.p_hp=p_hp
        self.p_str=p_str

assasin= karaktär(5, 10)
barb= karaktär(8, 7)
knight= karaktär(10, 5)

class monster():
    def _init_(self, m_hp, m_str):
        self.m_hp=m_hp
        self.m_str=m_str

slime= monster( m_health(4,11), m_damage(1,6))
goblin= monster( m_health(3,7), m_damage(3,8))

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

