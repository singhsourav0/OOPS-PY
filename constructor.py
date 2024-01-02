#Default consructor
class beu:
  def  __init__(self):
    self.name = "sourav"

  def print_name(self):
    print(self.name)


student = beu()
student.print_name()


#parametrized constructor:

class Addition:
  first = 0
  secound = 0
  answer = 0

  def __init__(self, f ,s):
    self.first = f
    self.secound =s

  def display(self):
     print("first number =" +str(self.first))
     print("secound number =" +str(self.secound))
     print("Additionof two numbers = " + str(self.answer))

  def calculate(self):
    self.answer =self.first +self.secound

num1 =Addition(1000, 200)
obj = Addition(10, 60)

num1.calculate()
obj.calculate()
num1.display()
obj.display()


#another example of parametrized constructor

class MyClass:
    def __init__(self, name=None):
        if name is None:
            print("Default constructor called")
        else:
            self.name = name
            print("Parameterized constructor called with name", self.name)
     
    def method(self):
        if hasattr(self, 'name'):
            print("Method called with name", self.name)
        else:
            print("Method called without a name")
 
# Create an object of the class using the default constructor
obj1 = MyClass()
 
obj1.method()
 
# Create an object of the class using the parameterized constructor
obj2 = MyClass("John")
obj2.method()
