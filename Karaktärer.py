class karaktär():
    def _init_(self, p_hp, spe, p_str):
        self.p_hp=p_hp
        self.spe=spe
        self.p_str=p_str

assasin= karaktär(3, 10, 7)
barb= karaktär(8,2,10)
knight= karaktär(10,6,4)

class monster():
    def _init_(self, m_hp, m_str):
        self.m_hp=m_hp
        self.m_str=m_str

slime= monster(1-4, 1-2)
goblin= monster(1-3, 2-4)
print("hej")