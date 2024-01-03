class emp(person):
  def print(self):
    print("emp class called ")

emp_details =emp("mayank" , 101)

#calling parent class function
emp_details.display()
#calling own class function
emp_details.print()

#***************************************
# parent class
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
 
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using its instance
a.display()

#*************************************************
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












