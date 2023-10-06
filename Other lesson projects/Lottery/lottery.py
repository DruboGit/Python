import random as r


prizes = [
    "Ticket to flight 11",
    "Time machine that only travels to the world trade center at september 11th 2001",
    "An expired n-word pass",
    "A crusty sock",
    "A guide to python v1.4",
    "Half a skateboard",
    "A singular particle of antimatter",
    "A year supply of vacuum",
    "A singular double A battery",
    "A leaf",
    "A significant amount of gaseous radon"
]
    
def get_prize():
    rand = r.randint(0, len(prizes)-1)
    return prizes[rand]