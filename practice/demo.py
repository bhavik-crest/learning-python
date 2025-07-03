if 5 < 2:
  print("Five is greater than two!")
else:
  print("Five is less than two!")

# This is a simple Python script to demonstrate basic syntax
# Variables and printing values
a = 200
b = "Bhavik"
print(a)
print(b)

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Python - Global Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This will return the items from index 0 to index 4.
# Remember that index 0 is the first item, and index 4 is the fifth item
# Remember that the item in index 4 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# This will return the items from index 2 to the end.
# Remember that index 0 is the first item, and index 2 is the third
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists in List
# To determine if a specified item is present in a list use the in keyword:
thislist = ["apples", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print("No, 'apple' is not in the fruits list")

# Change a Range of Item Values
# Example 1
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Example 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items method
# To insert a new item in the list, we can use the insert() method.
# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Python - Dictionaries
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "year": 2020,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway", gender = "Male")
print(thisdict)

# Python User Input
print("Enter your name:")
name = input()
print(f"Hello {name}")