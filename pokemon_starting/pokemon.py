# Class Pokemon 
class Pokemon:
    
    def __init__(self, names, level, type, maximum_health, current_health, is_knocked_down = False, exp = 0):
        self.name = names[0]
        self.level = level
        self.type = type
        self.maximum_health = maximum_health
        self.current_health = current_health
        self.is_knocked_down = is_knocked_down
        self.exp = exp
        self.names = names
    def __repr__(self):
        return """Information of {name}:\nLevel: {level}\nType: {type}\nHealth: {health}/{max_health}""".format(name = self.name, level = self.level, type = self.type, health = self.current_health, max_health = self.maximum_health)
    
    def lose_health(self, lost_health):
        self.current_health -= lost_health
        if self.current_health <= 0:
            self.knock_down()
        print(self.name + " now has " + str(self.current_health) + " health") 
    
    def gain_health(self, regain_health):
        self.current_health += regain_health
        if self.current_health >= self.maximum_health:
            self.current_health = self.maximum_health
        print(self.name + " now has " + str(self.current_health) + " health") 
    
    def knock_down(self):
        self.is_knocked_down = True
        print(self.name + " now has been knocked down") 
    
    def attack(self, other_pokemon):
        if self.is_knocked_down == True:
            print("{pokemon} is already knocked down")
        else:
            bonus = 0
            if self.type == "Fire" and other_pokemon.type == "Grass":
                bonus = 2
                print("{your_pokemon} is Fire while the opponent is Grass, damage deal will be double!".format(your_pokemon = self.name))
            elif self.type == "Grass" and other_pokemon.type == "Water":
                bonus = 2
                print("{your_pokemon} is Grass while the opponent is Water, damage deal will be double!".format(your_pokemon = self.name))
            elif self.type == "Water" and other_pokemon.type == "Fire":
                bonus = 2
                print("{your_pokemon} is Water while the opponent is Fire, damage deal will be double!".format(your_pokemon = self.name))
            else:
                bonus = 0.5
            damage = bonus * self.level
            print("{your_pokemon} deals {damage} damage to {opponent_pokemon}".format(your_pokemon = self.name, damage = damage, opponent_pokemon = other_pokemon.name))
            other_pokemon.lose_health(damage)
            if other_pokemon.is_knocked_down == True:
                if self.level - other_pokemon.level > 0:
                    coefficient = (self.level - other_pokemon.level)*0.5
                elif self.level - other_pokemon.level < 0:
                    coefficient = (other_pokemon.level - self.level)*2
                else:
                    coefficient = 1
                exp = coefficient*5
                self.gain_exp(exp)
    
    def gain_exp(self, exp):
        self.exp += exp
        print("{name} gains {exp} exp.".format(name = self.name, exp = exp))
        if self.exp >= 100:
            redundancy = self.exp - 100
            self.level += 1
            self.maximum_health += self.level*2
            self.exp = redundancy
            print("{name} gets level {lv}".format(name = self.name, lv = self.level))
        print("Experience of {name} now is: {exp}/100".format(name = self.name, exp = self.exp))
        print("{name}'s maximum health will be increased by {health}".format(name = self.name, health = self.level*2))
        if self.level == 16 or self.level == 36:
            self.evolve()
            
    def evolve(self):
        index = 0
        for i in range(len(self.names)):
            if self.names[i] == self.name:
                index = i + 1
        print("{name} is evolving to {name2} by getting level {level}".format(name = self.name, name2 = self.names[index], level = self.level))
        self.name = self.names[index]
        self.maximum_health += 100
        print("{name}'s maximum health will be increased by 100".format(name = self.name))

# Class Trainer
class Trainer:
    
    def __init__(self, pokemons, name, number_of_potions, currently_active_pokemon):
        if len(pokemons) <= 6:
            self.pokemons = pokemons
            self.name = name
            self.potions = number_of_potions
            self.currently_active_pokemon = currently_active_pokemon
        else:
            print("Trainer is just allowed to have maximum 6 pokemons!")
    
    def use_potion(self):
        if self.currently_active_pokemon.current_health == self.currently_active_pokemon.maximum_health:
            print("Can not use potion because {pokemon} is already full of health".format(pokemon = self.currently_active_pokemon.name))
        else:
            print("{trainer} is using potion to heal his {pokemon}".format(trainer = self.name, pokemon = self.currently_active_pokemon.name))
            for pokemon in self.pokemons:
                if pokemon.name == self.currently_active_pokemon.name:
                    pokemon.gain_health(100)
                    self.currently_active_pokemon = pokemon
                    break

    def attack_other_trainer(self, other_trainer):
        print("{trainer} is trying to attack {other_trainer}".format(trainer = self.name, other_trainer = other_trainer.name))
        for pokemon in other_trainer.pokemons:
            if pokemon.name == other_trainer.currently_active_pokemon.name:
                self.currently_active_pokemon.attack(pokemon)
                other_trainer.currently_active_pokemon = pokemon
                break

    def switch_another_pokemon(self, other_pokemon):
        for pokemon in self.pokemons:
            if pokemon.name == other_pokemon:
                if pokemon.is_knocked_down == True:
                    print("This pokemon is already knocked down, please switch to other pokemon!")
                else:
                    self.currently_active_pokemon = pokemon
                    print("{name} switched to {pokemon}".format(name = self.name, pokemon = other_pokemon))
                break

# Test above function
bulbasaur = Pokemon(["Bulbasaur","Ivysaur","Venusaur"], 1, "Grass", 50, 50)
charmander = Pokemon(["Charmander","Charmeleon","Charizard"], 1, "Fire", 50, 50)
squirtle = Pokemon(["Squirtle","Wartortle","Blastoise"], 1, "Water", 50, 50)
trainer_one = Trainer([bulbasaur, charmander, squirtle], "Alex", 4, squirtle)
trainer_two = Trainer([bulbasaur, charmander, squirtle], "John", 2, charmander)
trainer_one.attack_other_trainer(trainer_two)
trainer_two.use_potion()
trainer_two.switch_another_pokemon("Bulbasaur")
bulbasaur.evolve()
print(bulbasaur)