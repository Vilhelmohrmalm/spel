
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
    def __init__(self, p_hp, spe, p_str):
        self.p_hp=p_hp
        self.spe=spe
        self.p_str=p_str

# h

class monster():
    def __init__(self, m_hp, m_str, namn):
        self.namn = namn
        self.m_hp=m_hp
        self.m_str=m_str

    def __str__(self):
        return f"Det här är en {self.namn}, den har {self.m_hp} hp och {self.m_str} styrka"


slime= monster(m_health(1,4), m_damage(1,2), "slime")
goblin= monster(m_health(1,3), m_damage(2,4), "goblin")




        
def main():
    print(slime)
    print(goblin)

main()