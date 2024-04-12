from enum import Enum

class Stats:
    def __init__(self, Health : int, Attack : int, Defense : int, Sp_Attack : int, Sp_Defense : int, Speed : int):
        self.Health = Health
        self.Attack = Attack
        self.Defense = Defense
        self.Sp_Attack = Sp_Attack
        self.Sp_Defense = Sp_Defense
        self.Speed = Speed

class Element(Enum):
    Normal = 1
    Fighting = 2
    Flying = 3
    Poison = 4
    Ground = 5
    Rock = 6
    Bug = 7
    Ghost = 8
    Fire = 9
    Water = 10
    Grass = 11
    Electric = 12
    Psychic = 13
    Ice = 14
    Dragon = 15

class Pokemon:
    def __init__(self,id : int, name : str, element : Element, stats : Stats):
        