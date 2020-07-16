# Learning about inheritance

#Animal is the base class
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

#Mammal is derived class
class Mammal(Animal):
    def walk(self):
        print("walk")

#Fish is a derived class
class Fish(Animal):
    def swim(self):
        print("swim")

mammal = Mammal()
mammal.walk()
mammal.eat()

fish = Fish()
fish.eat()


print("Age of mammal is ", mammal.age)
print("Age of fish is ", fish.age)