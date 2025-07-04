def get_full_name(firstName: str, lastName: str, age: int):
     return f"{firstName.title()} {lastName.title()} is this old: {age}"

fname = "bill"
lname = "gates"
age = 67

print(get_full_name(fname, lname, age))