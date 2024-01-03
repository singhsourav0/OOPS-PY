# SOURAV KUMAR(SINGHSOURAV0)
# this repository is to demostrate the properties of inheritance....

# 1. The super function 

# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge)
 
obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()

#*************************************************
# 2. The adding properties.

# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Person):
  def __init__(self, name, age, dob):
    self.sName = name
    self.sAge = age
    self.dob = dob
    # inheriting the properties of parent class
    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge, self.dob)
 
obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()

#******************************************************

#3:- TYPES:
   #i. single inheritance:

class p(object):
  def __init__(self , name):
    self.name = name

  def getname(self):
    return self.name

  def isemployee(self):
    return False

class employee(p):
  def isemployee(self):
    return True

#driven code
emp= p("sourav")
print(emp.getname(), emp.isemployee())

emp = employee("mayank")
print(emp.getname(), emp.isemployee())
#*************************************************

# ii. multiple inheritances:-
 
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")
 
 
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
 
 
class Derived(Base1, Base2):
    def __init__(self):
 
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
 
    def printStrs(self):
        print(self.str1, self.str2)
 
 
ob = Derived()
ob.printStrs()

#****************************************************8
# multiple inheritance
 
# Base class1
class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
# Base class2
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
# Derived class
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"

#******************************************************

# iii:- multilevel inheritance

# Base class
 
 
class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
 
#intermediate
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)
 
# Derived class
 
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
 
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
 
 
#  Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()

#****************************************************

#iv:- Hierarchical Inheritance:

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")
 
# Derived class1
 
 
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
 
# Derivied class2
 
 
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
 
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

#**************************************************
#v Hybrid Inheritance:

class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
 
# Driver's code
object = Student3()
object.func1()
object.func2()

