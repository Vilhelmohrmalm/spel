from Karaktärer import *


class Vapen():
    def __init__(self, v_hp, v_str, v_namn):
        self.v_namn = v_namn
        self.v_hp = v_hp
        self.v_str = v_str


Svärd = Vapen(health(0, 1), damage(1, 5), "Svärd")
Sköld = Vapen(health(4, 8), damage(0, 0), "Sköld")
Yxa = Vapen(health(0, 0), damage(2, 6), "Yxa")
Pilbåge = Vapen(health(0, 0), damage(4, 5), "Pilbåge")
Spjut = Vapen(health(0, 0), damage(1, 7), "Spjut")
