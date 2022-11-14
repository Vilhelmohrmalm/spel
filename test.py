import random 

def m_health(a,b):
    health=[]
    for i in range(a,b+1):
        health.append(i)
    return(random.choice(health))

def m_damage(a,b):
    damage=[]
    for i in range(a,b+1):
        damage.append(i)
    return(random.choice(damage))


        
        
def main():
    print(m_health(4,11))
    print(m_damage(1,6))

main()