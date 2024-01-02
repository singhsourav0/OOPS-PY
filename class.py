class dog:

  pet1 = "mammal"
  pet2 = "tom"

  def fun(self):
    print("i'm a" , self.pet1)
    print("i'm a" , self.pet2)

Rodger = dog()

print(Rodger.pet1)
Rodger.fun()



class beu:
  def __init__(self,name,company):
    self.name    = name
    self.company = company

  def show(self):
    print("Hello my name is "+ self.name+ " and I study in "+ self.company + ".")

student = beu("sourav", "bpmce")
student.show()

#*************************************************************************8
class Dog:
  animal = 'dog'

  def __init__(self, breed, color):
    self.breed = breed
    self.color = color

Roadger = Dog("pug", "brown")
Buzo   = Dog("bulldog", "black")

print('Roadger details:')
print('Roadger is a', Roadger.animal)
print('Breed:' , Roadger.breed)
print('color:' ,Roadger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed:' ,Buzo.breed)
print('color:', Buzo.color)

print("\n Accessing class variable using class name")
print(Dog.animal)
