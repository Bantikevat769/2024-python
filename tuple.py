# Creating a tuple with different data types
my_tuple = (1, "Hello", 3.14, True)

# Accessing tuple elements
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: "Hello"
print(my_tuple[2])  # Output: 3.14
print(my_tuple[3])  # Output: True

# Slicing tuple elements

print(my_tuple[1:3])  # Output: ('Hello', 3.14)
print(my_tuple[:3])  # Output: (1, 'Hello', 3.14)
print(my_tuple[2:])  # Output: (3.14, True)
print(my_tuple[:])  # Output: (1, 'Hello', 3.14, True)

# Updating tuple elements
# Tuples are immutable, so we can't update individual elements. However, we can create a
# new tuple with the updated elements.




# count(value):
fruits = ("apple", "banana", "cherry", "banana")
banana_count = fruits.count("banana")
print(banana_count)  # Output: 2
# index(value, start, end):
fruits = ("apple", "banana", "cherry", "banana")
cherry_index = fruits.index("cherry")
print(cherry_index)  # Output: 2



# Using Tuples for Multiple Return Values:
def get_coordinates():
    return (10.0, 20.0)

coordinates = get_coordinates()
print(coordinates)  # Output: (10.0, 20.0)

# Tuples with One Element:

my_tuple = ("apple",)
print(my_tuple)  # Output: ('apple',)

# Unpacking Tuples:

coordinates = (10.0, 20.0)
x, y = coordinates
print(x)  # Output: 10.0
print(y)  # Output: 20.0

# Swapping Tuples:

a = 10
b = 20
a, b = b, a
print(a)  # Output: 20
print(b)  # Output: 10


# real life
# Employee Record
employee = ("John Doe", 30, "Software Engineer")

# Accessing Elements
print(f"Name: {employee[0]}")
print(f"Age: {employee[1]}")
print(f"Position: {employee[2]}")


# Advanced Concepts of Tuples
# Nested Tuples
nested_tuple = (1, 2, (3, 4), (5, 6, (7, 8)))

# Accessing Nested Tuple
print(nested_tuple[2])         # Output: (3, 4)
print(nested_tuple[3][2][1])   # Output: 8

# 2. Tuple Packing and Unpacking:
# Tuple Packing
packed_tuple = ("John", 25, "Developer")

# Tuple Unpacking
name, age, job = packed_tuple
print(f"Name: {name}, Age: {age}, Job: {job}")
# 3. Using Tuples as Dictionary Keys:

# Using tuple as a dictionary key
coordinates_dict = {
    (10.0, 20.0): "Point A",
    (30.0, 40.0): "Point B"
}

print(coordinates_dict[(10.0, 20.0)])  # Output: Point A

# 4. Tuples vs Lists in Memory Usage:
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"List memory size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple memory size: {sys.getsizeof(my_tuple)} bytes")
