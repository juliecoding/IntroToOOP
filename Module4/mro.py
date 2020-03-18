'''
    mro.py

    Illustrates the lookup order for the class
    hierarchy in Figure 9-5 (Module 5).

    Output:

    Cat Mammal LivingThing PhysicalObject object 
    Ant Insect LivingThing PhysicalObject object 
    Stone InanimateObject PhysicalObject object 
    Asteroid InanimateObject PhysicalObject object
'''

# Level 1
class PhysicalObject:
    pass

# Level 2
class LivingThing(PhysicalObject):
    pass

class InanimateObject(PhysicalObject):
    pass

# Level 3
class Mammal(LivingThing):
    pass

class Insect(LivingThing):
    pass

class Stone(InanimateObject):
    pass

class Asteroid(InanimateObject):
    pass

# Level 4
class Cat(Mammal):
    pass

class Ant(Insect):
    pass

def print_mro(clas):
    for c in clas.__mro__:
        print(c.__name__,end=" ")
    print()

# MROs for leaf classes
print_mro(Cat)
print_mro(Ant)
print_mro(Stone)
print_mro(Asteroid)
