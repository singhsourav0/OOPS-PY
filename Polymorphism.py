class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack! Quack!"

# Function demonstrating polymorphism
def animal_says(animal):
    return animal.speak()

# Creating instances of different classes
generic_animal = Animal()
my_dog = Dog()
my_cat = Cat()
my_duck = Duck()

# Calling the function with different objects
print("Generic Animal says:", animal_says(generic_animal))
print("My Dog says:", animal_says(my_dog))
print("My Cat says:", animal_says(my_cat))
print("My Duck says:", animal_says(my_duck))
