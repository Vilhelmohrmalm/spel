def fight(m_hp, m_str, p_hp, p_str):
    if p_str >= m_hp:
        print("du besegrade monstret")
        
        return
    elif p_str < m_hp and m_str >= p_hp:
        print("du dog")
    elif p_str < m_hp and m_str < p_hp:
        x= m_hp - p_str
        y= p_hp - m_str
        fight(x, m_str, y, p_str)
    
