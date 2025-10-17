class Pokemon():

    def __init__(self, number, name, type1, type2, hp, attack, defence, special_attack, special_defence, speed, ability):
        self.number = number
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.special_attack = special_attack
        self.special_defence = special_defence
        self.speed = speed
        self.ability = ability

    def intro(self):
        print(f"{self.number}: {self.name} ({self.type1} / {self.type2})")

clodsire = Pokemon(980, "Clodsire", "Poison", "Ground", 130, 75, 60, 45, 100, 20, "Poison Point")
slowking = Pokemon(199, "Slowking", "Water", "Psychic", 95, 75, 80, 100, 110, 30, "Oblivious")
clodsire.intro()
slowking.intro()