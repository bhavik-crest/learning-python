# Basics Variables
name = "Alice"
age = 20
print(name, age)

# Data Types
a = 10        # int (number)
b = 3.14      # float (decimal)
c = "hello"   # str (text)
d = True      # bool (true/false)

# Input and Output
name = input("Enter your name: ")
print("Hello, " + name)

# If / Else
age = 8
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Loops & Collections
# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 3:
    print("Hi")
    count += 1

# Lists
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple

# Dictionary
person = {"name": "John", "age": 25}
print(person["name"])   # John

# Functions
def greet(name):
    return "Hello, " + name

printFunction = greet("Alice")
print(printFunction)

# Classes (OOP)
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, I am", self.name)

p = Person("John")
p.say_hello()

# Exception Handling
try:
    num = int("abc")
except ValueError:
    print("Invalid number")
