# my_list = [element1, element2, element3]

fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4]
mixed_list = [1, 'apple', 3.14, True]

# 2. Accessing List Elements:

fruits = ['apple', 'banana', 'cherry']

print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry

# 3. Changing List Elements:

fruits = ['apple', 'banana', 'cherry']

fruits[0] = 'orange'

print(fruits)  # Output: ['orange', 'banana', 'cherry']

# 4. Adding List Elements:

fruits = ['apple', 'banana', 'cherry']

fruits.append('orange')

print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# 5. Removing List Elements:

fruits = ['apple', 'banana', 'cherry']

fruits.remove('banana')

print(fruits)  # Output: ['apple', 'cherry']

# 6. Sorting List Elements:

fruits = ['banana', 'apple', 'cherry']

fruits.sort()

print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 7. Reversing List Elements:

fruits = ['banana', 'apple', 'cherry']

fruits.reverse()

print(fruits)  # Output: ['cherry', 'apple', 'banana']

# 8. Finding List Elements:

fruits = ['apple', 'banana', 'cherry']

if 'apple' in fruits:
  print('apple is in the list')  # Output: apple is in the list

# 9. Counting List Elements:

fruits = ['apple', 'banana', 'cherry']

print(fruits.count('apple'))  # Output: 1

# 10. Looping List Elements:

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
  print(fruit)

# 11. Joining List Elements:  

fruits = ['apple', 'banana', 'cherry']

print(', '.join(fruits))  # Output: apple, banana, cherry 

# 12. Splitting List Elements:

fruits = ['apple', 'banana', 'cherry']

print(fruits[0])  # Output: apple

print(fruits[1])  # Output: banana

print(fruits[2])  # Output: cherry

# 13. Slicing List Elements:

fruits = ['apple', 'banana', 'cherry']  

print(fruits[:2])  # Output: ['apple', 'banana']

print(fruits[1:])  # Output: ['banana', 'cherry']

print(fruits[-2:])  # Output: ['banana', 'cherry']

print(fruits[:-1])  # Output: ['apple', 'banana']

# 14. Extending List Elements:

fruits = ['apple', 'banana', 'cherry']

fruits.extend(['orange', 'mango'])

print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'mango']

# 15. Indexing List Elements:

fruits = ['apple', 'banana', 'cherry']

print(fruits.index('banana'))  # Output: 1

# 16. Repeating List Elements:

fruits = ['apple', 'banana', 'cherry']

print(fruits * 3)  # Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']

# 17. Removing List Elements:

fruits = ['apple', 'banana', 'cherry']

del fruits[0]

print(fruits)  # Output: ['banana', 'cherry']

# 18. Clearing List Elements:

fruits = ['apple', 'banana', 'cherry']

fruits.clear()

print(fruits)  # Output: []

# 19. Copying List Elements:

fruits = ['apple', 'banana', 'cherry']

fruits_copy = fruits.copy()

print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']

# 20. Sorting List Elements:

fruits = ['banana', 'apple', 'cherry']

fruits.sort()

print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 21. Reversing List Elements:

fruits = ['banana', 'apple', 'cherry']

fruits.reverse()

print(fruits)  # Output: ['cherry', 'apple', 'banana']

# 22. Counting List Elements:

fruits = ['apple', 'banana', 'cherry']

print(fruits.count('apple'))  # Output: 1

# 23. Looping List Elements:

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
  print(fruit)

# 24. Joining List Elements:

fruits = ['apple', 'banana', 'cherry']

print(', '.join(fruits))  # Output: apple, banana, cherry

# 25. Splitting List Elements:

fruits = ['apple', 'banana', 'cherry']

print(fruits[0])  # Output: apple

print(fruits[1])  # Output: banana

print(fruits[2])  # Output: cherry


# 7. Nested Lists:

fruits = ['apple', 'banana', ['cherry', 'mango']]

print(fruits[2][0])  # Output: cherry

print(fruits[2][1])  # Output: mango

numbers = [1, 2, 3, 4, 5]

# len() to get length of list
print(len(numbers))  # Output: 5

# max() to get the maximum value
print(max(numbers))  # Output: 5

# sum() to get the sum of elements
print(sum(numbers))  # Output: 15

# any() example
bool_list = [False, False, True]
print(any(bool_list))  # Output: True

# all() example
print(all([1, 2, 3]))  # Output: True
print(all([0, 1, 2]))  # Output: False
# 9. List Comprehension:
