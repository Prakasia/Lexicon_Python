"""
4.  BUILD POLYMORPHISM WITH INHERITANCE
Objective: Understand method overriding and runtime dispatch.
**************************************************************
Instructions:
1. Design a base class representing a general concept.
2. The base class must define a method but not implement it.
3. Create at least three subclasses that:
    o inherit from the base class
    o override the method with different behavior
4. Write a function that:
    o accepts the base class
    o calls the method
    o does NOT use conditionals
5. Call the function with each subclass.
Constraints
• Do NOT use if, elif, or isinstance
"""

class Travel:
    def route(self):
        NotImplemented

class Bus(Travel):
    def route(self):
        return 'Road'
    
class Cruise(Travel):
    def route(self):
        return 'Sea'
    
class Jet(Travel):
    def route(self):
        return 'Air'
    
def routeOfTravel(travel):
    return travel.route()

print(routeOfTravel(Bus()))
print(routeOfTravel(Cruise()))
print(routeOfTravel(Jet()))