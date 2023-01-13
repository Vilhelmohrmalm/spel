import random
from karaktär import *




def fight(spelar_stats, monster_stats):

    if spelar_stats.p_str >= monster_stats.m_hp:
        print("du besegrade monstret")
        print(f"Du har {spelar_stats.p_hp} kvar")

    elif spelar_stats.p_str < monster_stats.m_hp and monster_stats.m_str >= spelar_stats.p_hp:
        print("du dog")
    elif spelar_stats.p_str < monster_stats.m_hp and monster_stats.m_str < spelar_stats.p_hp:
        monster_stats.m_hp = monster_stats.m_hp - spelar_stats.p_str
        spelar_stats.p_hp= spelar_stats.p_hp - monster_stats.m_str
        fight(spelar_stats, monster_stats)

