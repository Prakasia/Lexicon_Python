# ZOO SIMULATION SYSTEM (PYTHON - OOP)

## 📌 PROJECT OVERVIEW  
This project is an object-oriented zoo simulation implemented in Python.
It models animals, their behaviors, and interactions with visitors over the course of a simulated day in a zoo.

The goal of the project is to demonstrate core Object-Oriented Programming (OOP) concepts such as inheritance, encapsulation, method overriding, and polymorphism in a clear and practical way.

## CLASS DESIGN

### 1. Animal (Base Class)
Generic animal in the zoo with attributes
- name : Name of animal
- age : Age of animal
- species : species name
- _energy_level : protected attribute with the current energy level

** Methods: **
- eat() : Increases energy level 
- sleep() : Increases additional energy
- status() : Display the current status of the animal

### 2. Herbivores and Carnivores (Subclasses)
Both classes inherit from the * Base class Animal * 
- Reuse base functionality
- Overrides eat() and sleep() methods

### 3. Visitor
Represents a visitor interacting with the animal 
** Attribute : ** name - Name of the visitor
** Method ** feed(animal) - Feeds the animal by calling eat() method

## 🔄 SIMULATION FLOW
### 1. Morning
- Zoo opens 
- Initial status of all animals displayed

### 2. Feeding Time
- Zookeeper feeds all the animals
- Energy level increases
- Display the status of all animals

### 3. Visitor Interaction
- Visitor feeds a selected animal

### 4. Evening
- Sleeping time
- Energy level increases further
- Display the status
