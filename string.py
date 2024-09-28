
# Python String Methods Examples

# 1. len() - Returns the length of the string.
text = "Hello, World!"
length = len(text)
print(length)  # Output: 13

# 2. lower() - Converts all characters to lowercase.
text = "Hello, World!"
print(text.lower())  # Output: hello, world!

# 3. upper() - Converts all characters to uppercase.
text = "Hello, World!"
print(text.upper())  # Output: HELLO, WORLD!

# 4. strip() - Removes whitespace from the beginning and end of the string.
text = "   Hello, World!   "
print(text.strip())  # Output: Hello, World!

# 5. replace(old, new) - Replaces a substring with another substring.
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)  # Output: Hello, Python!

# 6. split(separator) - Splits the string into a list using the specified separator.
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# 7. join(iterable) - Joins the elements of a list into a single string with a specified separator.
fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)
print(result)  # Output: apple, banana, cherry

# 8. find(substring) - Returns the index of the first occurrence of the substring, or -1 if not found.
text = "Hello, World!"
position = text.find("World")
print(position)  # Output: 7

# 9. count(substring) - Returns the count of occurrences of the substring.
text = "Hello, World! Hello, Python!"
count = text.count("Hello")
print(count)  # Output: 2

# 10. startswith(prefix) - Checks if the string starts with the specified prefix.
text = "Hello, World!"
print(text.startswith("Hello"))  # Output: True

# 11. endswith(suffix) - Checks if the string ends with the specified suffix.
text = "Hello, World!"
print(text.endswith("World!"))  # Output: True

# 12. capitalize() - Capitalizes the first character of the string.
text = "hello, world!"
print(text.capitalize())  # Output: Hello, world!

# 13. title() - Capitalizes the first character of each word in the string.
text = "hello, world!"
print(text.title())  # Output: Hello, World!

# 14. isdigit() - Checks if the string consists only of digits.
number = "12345"
print(number.isdigit())  # Output: True

# 15. isalpha() - Checks if the string consists only of alphabets.
word = "Hello"
print(word.isalpha())  # Output: True

# 16. isalnum() - Checks if the string consists only of alphabets or digits.
alphanumeric = "Hello123"
print(alphanumeric.isalnum())  # Output: True

# 17. format() - Formats the string by inserting variables.
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is John and I am 30 years old.

# 18. f-strings - A newer way to format strings using f-strings.
print(f"My name is {name} and I am {age} years old.")
# Output: My name is John and I am 30 years old.

# 19. zfill(width) - Pads the string with zeros to the specified width.
number = "42"
print(number.zfill(5))  # Output: 00042

# 20. swapcase() - Swaps the case of all characters in the string.
text = "Hello, World!"
print(text.swapcase())  # Output: hELLO, wORLD!

# 21. index(substring) - Returns the index of the first occurrence of the substring.
text = "Hello, World!"
position = text.index("World")
print(position)  # Output: 7

# 22. rfind(substring) - Returns the index of the last occurrence of the substring, or -1 if not found.
text = "Hello, World! Hello, Python!"
position = text.rfind("Hello")
print(position)  # Output: 20

# 23. count(substring) - Returns the count of occurrences of the substring.
text = "Hello, World! Hello, Python!"
count = text.count("Hello")
print(count)  # Output: 2

name = "Ramesh"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)


