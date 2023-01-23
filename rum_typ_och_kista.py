from text_animering import *

def slut():
    typingPrint("Game Over")
    quit()

def boss_fight(spelar_stats):
    typingPrint("Nu har du nått sista kammaren men där väntar Taurus\n Hans massiva slimekapacitet har gett honom en hp på 30 och en styrka på 10\n")
    m_hp = 30
    m_str = 10
    val = typingInput("S = sloss mot Taurus\nL = ge upp\n")
    while m_hp == 30:
        if val in ["S", "s", "sloss", "sloss mot Taurus"]:
            while m_hp > 0:
                if spelar_stats.p_str + spelar_stats.vapen.v_str >= m_hp:
                    typingPrint("Du besegrade tarus och kan änligen lämna labyrinten\n")
                    return (spelar_stats)

                elif spelar_stats.p_str + spelar_stats.vapen.v_str < m_hp and m_str >= spelar_stats.p_hp + spelar_stats.vapen.v_hp:
                    typingPrint(f"Taurus dödade dig\nMåste vara skill issue\n")
                    slut()
                elif spelar_stats.p_str + spelar_stats.vapen.v_str < m_hp and m_str < spelar_stats.p_hp + spelar_stats.vapen.v_hp:
                    m_hp = m_hp - \
                        spelar_stats.p_str - spelar_stats.vapen.v_str
                    spelar_stats.p_hp = spelar_stats.p_hp - \
                        m_str + spelar_stats.vapen.v_hp
        elif val in ["L", "l", "ge upp"]:
            typingPrint("Du gav upp och dog på lvl 30\nMsåst vara skill issue\n")
            slut()
        else: typingPrint("Din sopa välj ett av alternativen\n")



class Karaktärer():
    def __init__(self, p_hp, p_str, p_lvl, p_lvlpoäng, p_namn, vapen):
        self.p_hp = p_hp
        self.p_str = p_str
        self.p_lvl = p_lvl
        self.p_lvlpoäng = p_lvlpoäng
        self.p_namn = p_namn
        self.vapen = vapen


class Vapen():
    def __init__(self, v_hp, v_str, v_namn):
        self.v_namn = v_namn
        self.v_hp = v_hp
        self.v_str = v_str

Start = Vapen(0, 0, "en pinne")
Assasin = Karaktärer(10, 15, 0, 0, "assasin", Start)


def main():
    spelar_stats = (Assasin)
    boss_fight(spelar_stats)
main()
