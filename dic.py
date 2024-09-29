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


