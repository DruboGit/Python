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
    def __init__(self,id : int, name : str, element : list, stats : Stats):
        self.id = id
        self.name = name
        self.element = element
        self.stats = stats

Bulbasaur = Pokemon(1, "Bulbasaur", [Element.Grass, Element.Poison], Stats(45, 49, 49, 65, 65, 45))
Pikachu = Pokemon(25, "Pikachu", [Element.Electric], Stats(35, 55, 30, 50, 40, 90))
Lickitung = Pokemon(108, "Lickitung", [Element.Normal], Stats(90, 55, 75, 60, 75, 30))
Mr_Mime = Pokemon(122, "Mr. Mime", [Element.Psychic], Stats(40, 45, 65, 100, 120, 90))
Magikarp = Pokemon(129, "Magikarp", [Element.Water], Stats(20, 10, 55, 15, 20, 80))
Ditto = Pokemon(132, "Ditto", [Element.Normal], Stats(48, 48, 48, 48, 48, 48))
Mewtwo = Pokemon(150, "Mewtwo", [Element.Psychic], Stats(106, 110, 90, 154, 90, 130))

class Trainer:
    def __init__(self, name : str, gender : str, age : int, inventory : list, party : list):
        self.name = name
        self.gender = gender
        self.age = age
        self.inventory = inventory
        self.party = party

random_names = ["Alloush", "Amin", "Angelo", "Anton", "Elias", "Emil", "Fabian", "Filippa", "Melvin", "Nils", "Rasmus", "Ron", "Wille"]
random_genders = ["helicopter", "plane", "male", "female", "invisible person", "Ronald"]