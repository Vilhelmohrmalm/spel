from Karaktärer import *
import random

def fight( p_hp, p_str):
    monster=random.randint(1, 2)
    if monster == 1:
        m_hp = health(4, 11)
        m_str = damage(1,6)
        print(f"Du stöter på en slime med hp {m_hp} och str {m_str}")
    elif monster==2:
        m_hp = health(3, 7)
        m_str= damage(3,8)
        print(f"Du stöter på en goblin med hp {m_hp} och str {m_str}")
    if p_str >= m_hp:
        print("du besegrade monstret")
        print(f"Du har {p_hp} kvar")
        return (p_hp)
    elif p_str < m_hp and m_str >= p_hp:
        print("du dog")
    elif p_str < m_hp and m_str < p_hp:
        m_hp = m_hp - p_str
        p_hp = p_hp - m_str
        fight(m_str, m_str, p_hp, p_str)

