"""
energy level is the protected attribute

"""
TABLE_LINE = '\033[1;34;40m|\033[0m'
TABLE_STAR = '\033[1;34;40m*\033[0m'
TABLE_UNDERLINE = '\033[1;34;40m-\033[0m'
TABLE_HEADER_COLOR = '\033[1;34;40m'
RED_TEXT = '\033[0;31;40m'
RESET = '\033[0m'

# CONSTANTS USED FOR ENERGY CALCULATION
MAX_ENERGY = 100
DEFAULT_ENERGY = 40

# BASE CLASS ANIMAL
class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'default_name')
        self.age = kwargs.get('age', 0)
        self.species = kwargs.get('species','default_species')
        self._energy_level = kwargs.get('energy_level', DEFAULT_ENERGY)

    # PROTECTED METHOD TO CALCULATE ENERGY
    def _calculate_energy(self, delta):
        old = self._energy_level
        self._energy_level = max(0, min(MAX_ENERGY, old + delta))
        return old, self._energy_level
    
    # METHOD TO RETURN THE STATUS OF EACH ANIMAL
    def status(self):
        return TABLE_LINE.join(f'{value:^15}' for key, value in self.__dict__.items())

    # ANIMAL EAT METHOD CALCULATES THE ENERGY
    def eat(self):
        old, self._energy_level = self._calculate_energy(5)
        return f'is eating.\n Energy level {RED_TEXT}{old} -> {self._energy_level}{RESET}'
    
    # ANIMAL SLEEP METHOD INCREASES THE ENERGY
    def sleep(self):
        old = self._energy_level
        self._energy_level = min(self._energy_level+10, MAX_ENERGY)
        return f'Energy level {RED_TEXT}{old} -> {self._energy_level}{RESET}'
    
    # PLAYING WITH OTHER ANIMALS
    def play_with_other(self):
        old_self, self._energy_level = self._calculate_energy(-7)
        return f'Energy : {RED_TEXT}{old_self} -> {self._energy_level}{RESET}'


# SUBCLASS HERBIVORE
class Herbivores(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def eat(self):
        tx = super().eat()
        return f' {self.name} the {self.species} {tx}'
    
    def sleep(self):
        return f' {self.name} is taking a good nap !! \n {super().sleep()}'
    
    def play_with_other(self, other):
        txt = super().play_with_other()
        old_other, new_other = other._calculate_energy(-7)
        return f'{self.name} played with {other.name}\n {self.name} {txt}\n {other.name} Energy : {RED_TEXT}{old_other} -> {new_other}{RESET}'

# SUBCLASS CARNIVORES
class Carnivores(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def eat(self):
        tx = super().eat()
        return f' {self.name} the {self.species} {tx}'

    def sleep(self):
        return f' {self.name} is taking a good nap !! \n {super().sleep()}'
    
    def play_with_other(self, other):
        txt = super().play_with_other()
        old_other, new_other = other._calculate_energy(-6)
        return f'{self.name} played with {other.name}\n {self.name} {txt}\n {other.name} Energy : {RED_TEXT}{old_other} -> {new_other}{RESET}'



# VISITOR CLASS INTERACTING WITH THE ANIMAL BASE CLASS NOT DIRECTLY WITH SUBCLASSES
class Visitor:
    def __init__(self,name):
        self.name = name

    def feed(self, animal):
        return f'{self.name} feeds {animal.name}\n{animal.eat()}'
    
