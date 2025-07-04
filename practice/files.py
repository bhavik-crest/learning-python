# This script demonstrates how to create, write to, and read from a file in Python.
f = open("demofile.txt", "r")
print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this:
# f = open("D:\\myfiles\demofile.txt")
# print(f.read())

# with open("demofile.txt", "r") as f:
# print(f.read())

f = open("demofile.txt")
print(f.readline())
print(f.readline())
f.close()