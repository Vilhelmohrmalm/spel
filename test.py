
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
    def __init__(self, p_hp, p_str,p_namn):
        self.p_hp=p_hp
        self.p_str=p_str
        self.p_namn=p_namn

# h

class monster():
    def __init__(self, m_hp, m_str,m_namn):
        self.namn =m_namn
        self.m_hp=m_hp
        self.m_str=m_str

    def __str__(self):
        return f"Det här är en {self.m_namn}, den har {self.m_hp} hp och {self.m_str} styrka"


slime= monster(m_health(4,11), m_damage(1,6), "slime")
goblin= monster(m_health(1,3), m_damage(2,4), "goblin")




        
def main():
    print(slime)
    print(goblin)

main()