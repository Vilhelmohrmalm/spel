from karaktär import *
import random




def fight(spelar_stats, monster_stats):

    if spelar_stats.p_str >= m_hp:
        print("du besegrade monstret")
        print(f"Du har {p_hp} kvar")

    elif spelar_stats.p_str < m_hp and m_str >= spelar_stats.p_hp:
        print("du dog")
    elif spelar_stats.p_str < m_hp and m_str < spelar_stats.p_hp:
        monster_stats.m_hp = m_hp - spelar_stats.p_str
        spelar_stats.p_hp= spelar_stats.p_hp - m_str
        fight(spelar_stats, monster_stats)

