# Create a Class
class MyClass:
  x = 5

print(MyClass)

# Create Object
p1 = MyClass()
print(p1.x)

# The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#The __str__() Function
  def __str__(self):
    return f"{self.name}({self.age})"

# Object Methods
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Bhavik", 25)

# Modify Object Properties
p1.age = 24

print(p1)
print(p1.age)
p1.myfunc()




#######################################
# Python Inheritance
#######################################
# Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
# x = Person("John", "Doe")
# x.printname()

# Create a Child Class
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    #Add Properties
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
  #pass

x = Student("Mike", "Olsen", 2020)
#print(x.graduationyear)
x.welcome()
#######################################




#######################################
# Python Iterators
#######################################
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# for x in mystr:
#   print(x)

# Create an Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
#######################################




#######################################
# Python Polymorphism
#######################################
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
#######################################




#######################################
# Python Lambda
#######################################

# Syntax -> lambda arguments : expression

#Example 1: A simple lambda function that adds 10 to the input value
x = lambda a : a + 10 
print(x(5))  # Output: 15

# Lambda functions can take any number of arguments:
# Example 2: Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))  # Output: 30

# Example 3: Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))  # Output: 13