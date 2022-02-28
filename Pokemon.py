#Create a class
class Pokemon:
    def __init__(self, name, species, evolve, level, power=100):
        self.name = name
        self.species = species
        self.evolve = evolve
        self.level = level
        self.power = power
        

    def evolution(self): 
        print(self.name + self.species +" "+ " evolves into " + self.evolve +" "+ self.level)
    def Moves(self):
        self.power -= 40
    # def power(self, moves):
    #     self.moves = moves

p1 = Pokemon("Charmander: ", "Fire,", "Charmeleon", "at level 16")
p1.evolution()
#p1.Moves("Tail Whip")
p2 = Pokemon("Pikachu: ", "Electric,", "Raichu", "once it has the Thunder Stone")
p2.evolution()
p3 = Pokemon("Magikarp: ", "Water,", "Gyarados", "at level 20")
p3.evolution()
p4 = Pokemon("Eevee: ", "Normal,",  "Flareon", "with Fire Stone")
p4.evolution()





