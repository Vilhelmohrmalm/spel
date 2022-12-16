def fight(m_hp, m_str, p_hp, p_str):
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

