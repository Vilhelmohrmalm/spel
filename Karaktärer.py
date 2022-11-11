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

slime= monster(4-11, 1-6)
goblin= monster(3-7, 3-8)
