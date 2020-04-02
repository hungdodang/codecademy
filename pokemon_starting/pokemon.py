# Class Pokemon 
class Pokemon:
    def __init__(self, name, level, type, maximum_health, current_health, is_knocked_down = False):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = maximum_health
        self.current_health = current_health
        self.is_knocked_down = is_knocked_down
    def lose_health(self, lost_health):
        self.current_health -= lost_health
        if self.current_health <= 0:
            self.knock_down()
        print(self.name + " now has " + str(self.current_health) + " health") 
    def regain_health(self, regain_health):
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
                    pokemon.regain_health(100)
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
bulbasaur = Pokemon("Bulbasaur", 50, "Grass", 400, 400)
charmander = Pokemon("Charmander", 50, "Fire", 400, 400)
squirtle = Pokemon("Squirtle", 50, "Water", 400, 400)
trainer_one = Trainer([bulbasaur, charmander, squirtle], "Alex", 4, squirtle)
trainer_two = Trainer([bulbasaur, charmander, squirtle], "John", 2, charmander)
trainer_one.attack_other_trainer(trainer_two)
trainer_two.use_potion()
trainer_two.switch_another_pokemon("Bulbasaur")
trainer_two.use_potion()