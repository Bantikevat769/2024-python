# Dictionary ka Syntax aur Basic Structure
student = {
    "name": "Banti", 
    "age": 21, 
    "course": "Computer Science"
}
# Dictionary ke Methods aur Operations

# Accessing Values (Value ko fetch karna)

# Square Brackets
print(student["name"])  # Output: Banti

# get() Method
print(student.get("age"))  # Output: 21

# Adding or Updating Key-Value Pair (Nayi entry ya update karna)

# Square Brackets
student["city"] = "Delhi"
print(student)  # Output: {'name': 'Banti', 'age': 21, 'course': 'Computer Science', 'city': 'Delhi'}

# Removing Items (Items ko remove karna)

# del
del student["city"]
print(student)  # Output: {'name': 'Banti', 'age': 21, 'course': 'Computer Science'}

# pop()
student.pop("age")
print(student)  # Output: {'name': 'Banti', 'course': 'Computer Science'}

# popitem()
student.popitem()
print(student)  # Output: {'name': 'Banti'}

# clear()
student.clear()
print(student)  # Output: {}

# Looping through Dictionary (Loop lagana)
students = {
    "name": "John", 
    "age": 21, 
    "course": "Computer Science"
}

for key in students:
    print(key, ":", students[key])

for value in students.values():
    print(value)

for key, value in students.items():
    print(key, ":", value)

# Dictionary ke Methods aur Operations

# len()
print(len(students))  # Output: 3

# copy()
new_students = students.copy()
print(new_students)  # Output: {'name': 'John', 'age': 21, 'course': 'Computer Science'}

# fromkeys()
keys = ["name", "age", "course"]
new_students = dict.fromkeys(keys)
print(new_students)  # Output: {'name': None, 'age': None, 'course': None}

# get()
print(students.get("name"))  # Output: John

# setdefault()  
print(students.setdefault("name"))  # Output: John
print(students.setdefault("age"))  # Output: 21
print(students.setdefault("course"))  # Output: Computer Science
print(students)  # Output: {'name': 'John', 'age': 21, 'course': 'Computer Science'}

# update()
students.update({"name": "Banti", "age": 22, "course": "Computer Science"})
print(students)  # Output: {'name': 'Banti', 'age': 22, 'course': 'Computer Science'}

# keys()
print(students.keys())  # Output: dict_keys(['name', 'age', 'course'])

# values()  
print(students.values())  # Output: dict_values(['Banti', 22, 'Computer Science'])

# items()
print(students.items())  # Output: dict_items([('name', 'Banti'), ('age', 22), ('course', 'Computer Science')])

# clear()
students.clear()
print(students)  # Output: {}

data = {
    "name": "John", 
    "age": 21, 
    "course": "Computer Science"
}

# Checking Existence (Key exist karti hai ya nahi)
if "name" in data:
    print("Key 'name' exists!")

# Checking Existence (Value exist karti hai ya nahi)
if "John" in data.values():
    print("Value 'John' exists!")

# Checking Existence (Key and Value exist karti hai ya nahi)
if "name" in data and "John" in data.values():
    print("Key 'name' and value 'John' exist!")


# 2. Dictionary Comprehension
# Dictionary Comprehension is a concise and powerful way to create dictionaries from lists.
numbers = [1, 2, 3, 4, 5]
square = {num: num**2 for num in numbers}
print(square)

# 3. Merging Dictionaries Using | Operator - Python 3.9+
a = {1, 2, 3}
b = {4, 5, 6}
c = a | b
print(c)  # Output: {1, 2, 3, 4, 5, 6}  

# 4. Merging Dictionaries Using update() Method
a = {1, 2, 3}
b = {4, 5, 6}
a.update(b)
print(a)  # Output: {1, 2, 3, 4, 5, 6}

# 5. Nested Dictionaries

data = {
    "name": "John",
    "age": 21,
    "address": {
        "street": "Main Street",
        "city": "New York",
        "country": "USA"
    }
}

print(data["address"]["city"])  # Output: New York

# 6. Dictionary with Default Values
data = {
    "name": "John",
    "age": 21
}

print(data.setdefault("city", "New York"))  # Output: New York  

# 7. Dictionary with Multiple Data Types
data = {
    "name": "John",
    "age": 21,
    "phone": 1234567890
}

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': 1234567890}

# 8. Dictionary with Duplicate Keys
data = {
    "name": "John",
    "age": 21,
    "name": "Jane"
}

print(data)  # Output: {'name': 'Jane', 'age': 21}

# 9. Dictionary with Empty Values
data = {
    "name": "John",
    "age": 21,
    "address": None
}

print(data)  # Output: {'name': 'John', 'age': 21, 'address': None}

# 10. Dictionary with None Values
data = {
    "name": "John",
    "age": 21,
    "phone": None
}

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': None} 

# 11. Dictionary with Nested Lists  

data = {
    "name": "John",
    "age": 21,
    "phone": [1234567890, 9876543210]
} 

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': [1234567890, 9876543210]}

# 12. Dictionary with Nested Dictionaries

data = {
    "name": "John",
    "age": 21,
    "address": {
        "street": "Main Street",
        "city": "New York",
        "country": "USA"
    }
}

print(data)  # Output: {'name': 'John', 'age': 21, 'address': {'street': 'Main Street', 'city': 'New York', 'country': 'USA'}}

# 13. Dictionary with Nested Tuples

data = {
    "name": "John",
    "age": 21,
    "phone": (1234567890, 9876543210)
} 

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': (1234567890, 9876543210)}

# 14. Dictionary with Nested Sets

data = {
    "name": "John",
    "age": 21,
    "phone": {1234567890, 9876543210}
}

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': {1234567890, 9876543210}}

# 15. Dictionary with Nested Frozen Sets..

data = {
    "name": "John",
    "age": 21,
    "phone": frozenset({1234567890, 9876543210})
} 

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': frozenset({1234567890, 9876543210})}

# 16. Dictionary with Nested Functions

data = {
    "name": "John",
    "age": 21,
    "phone": lambda: 1234567890
}

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': <function __main__.<lambda>()>}

# 17. Dictionary with Nested Classes

data = {
    "name": "John",
    "age": 21,
    "phone": Phone
}

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': <class '__main__.Phone'>}

# 18. Dictionary with Nested Modules

data = {
    "name": "John",
    "age": 21,
    "phone": phone
}

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': <module 'phone' from 'phone.py'>}

# 19. Dictionary with Nested Iterables

data = {
    "name": "John",
    "age": 21,
    "phone": [1234567890, 9876543210]
}

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': [1234567890, 9876543210]}

# 20. Dictionary with Nested Generators

data = {
    "name": "John",
    "age": 21,
    "phone": (1234567890, 9876543210)
}

print(data)  # Output: {'name': 'John', 'age': 21, 'phone': (1234567890, 9876543210)}