"""
            PROJECT :  ZOO SIMULATION SYSTEM
            ********************************
Core Functionalities:
- Implement an object-oriented zoo simulation system.
- Include a base Animal class with common attributes such as name, age, and energy level.
- Include subclasses for different animal types (for example Herbivores and Carnivores).
- Implement at least three concrete animal species with unique behaviors.
- Include a Visitor class that can interact with animals (for example feeding them).
- Simulate at least one full day in the zoo where animals eat, sleep, and interact.
- Demonstrate inheritance and method overriding.
- The program must run without errors and clearly show the simulation flow through output.
"""

import func_classes as cl
import random

TEXT_LEN  = 65
TEXT_COLOR_CYAN = '\033[1;36;40m'
TEXT_COLOR_CYAN_IT = '\033[3;36;40m'

def print_status():
    text = f'{cl.TABLE_HEADER_COLOR}|{"NAME":^15}|{cl.TABLE_HEADER_COLOR}{"AGE":^15}|{cl.TABLE_HEADER_COLOR}{"SPECIES":^15}|{cl.TABLE_HEADER_COLOR}{"ENERGY LEVEL":^15}|\033[0m'
    print(text)
    print(cl.TABLE_STAR*TEXT_LEN)
    for animal in animals:
        print(f'{cl.TABLE_LINE}{animal.status()}')
    print(cl.TABLE_UNDERLINE*TEXT_LEN)

l = {
    "name" : 'Simba', 
    "species" : "Lion",
    "age" : 5, 
    "energy_level": 35
}

d = {
    "name":'Bambi',
    "species" : 'Deer',
    "age" : 6,
    "energy_level" : 40
}  

g = {
    "name" : 'Sky',
    "species" : 'Giraffe',
    "age" : 4,
    "energy_level" : 30
}

t = {
    "name" : 'Caspian',
    "species" : 'Tiger',
    "age" : 8,
    "energy_level" : 43
}

r = {
    "name" : 'Peter',
    "species" : 'Rabbit',
    "age" : 4,
    "energy_level" : 50
}

f = {
    "name" : 'Foxy',
    "species" : 'Fox',
    "age" : 8,
    "energy_level" : 48
}

lion = cl.Carnivores(**l)
deer = cl.Herbivores(**d)
giraffe = cl.Herbivores(**g)
tiger = cl.Carnivores(**t)
rabbit = cl.Herbivores(**r)
fox = cl.Carnivores(**f)

# ANIMALS LIST
animals = [lion, deer, giraffe, tiger, rabbit, fox]
# VISITOR LIST
visitorslist = ['Anna', 'Bob', 'Alice', 'Mo', 'Jo', 'Lee']

# WELCOME MESSAGE
text = " WELCOME TO JUNGLE KINGDOM "
print(f'\033[1;32;40m {text:=^80} {cl.RESET}')

# LOOP FOR SIMULATING N NUMBER OF DAYS Here N = 4
for d in range (1,5):
    text = f'Day{d}'
    print(f'{TEXT_COLOR_CYAN_IT}{text:^80}{cl.RESET}')
    print(' Good Morning :) All animals are awake!! \n Below is the current status of all animals')
    # PRINT THE STATUS OF ANIMALS - MORNING
    print_status()

    # EATING - FEEDING ALL THE ANIMALS IN MORNING
    print(f'{TEXT_COLOR_CYAN}FEEDING TIME : {cl.RESET}',end="")
    print(f'{TEXT_COLOR_CYAN_IT}Zookeeper feeds all the animals{cl.RESET}')
    for animal in animals:
        print(animal.eat())
    # STATUS AFTER EATING
    # print_status()

    visitor1 = cl.Visitor(random.choice(visitorslist))
    visitor2 = cl.Visitor(random.choice(visitorslist))
    # VISITOR INTERACTION TIME
    print(f'{TEXT_COLOR_CYAN}VISITOR INTERACTION TIME : {cl.RESET}',end="")
    print(f'{TEXT_COLOR_CYAN_IT}Visitors can feed the animals now{cl.RESET}')

    print(visitor1.feed(random.choice(animals)))
    print(visitor2.feed(random.choice(animals)))
    # print_status()

    # PLAY TIME
    print(f'{TEXT_COLOR_CYAN}PLAY TIME : {cl.RESET}',end="")
    print(f'{TEXT_COLOR_CYAN_IT}Play time for animals{cl.RESET}')
    print(lion.play_with_other(tiger))
    print(deer.play_with_other(giraffe))

    # SLEEPING TIME
    print(f'{TEXT_COLOR_CYAN}SLEEPING TIME : {cl.RESET}',end="")
    print(f'{TEXT_COLOR_CYAN_IT}Evening sleeping time{cl.RESET}')
    for animal in animals:
        print(animal.sleep())
    # STATUS AFTER SLEEPING
    print_status()









