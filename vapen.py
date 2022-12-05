from Karaktärer import *


class Vapen():
    def __init__(self, v_hp, v_str, v_namn):
        self.v_namn = v_namn
        self.v_hp = v_hp
        self.v_str = v_str


Svärd = Vapen(health(0, 1), damage(1, 4), "svärd")
Sköld = Vapen(health(2, 3), damage(0, 1), "sköld")
