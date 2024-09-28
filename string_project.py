def advanced_text_processor():
    print("Welcome to the Advanced Text Processor!")
    text = input("Enter the text you want to process: ")
    
    while True:
        print("\nSelect an operation to perform:")
        print("1. Capitalize text")
        print("2. Casefold text")
        print("3. Center text")
        print("4. Count substring")
        print("5. Check if text ends with a suffix")
        print("6. Check if text starts with a prefix")
        print("7. Expand tabs")
        print("8. Find a substring")
        print("9. Get the index of a substring")
        print("10. Check if text is alphanumeric")
        print("11. Check if text is alphabetic")
        print("12. Check if text is numeric")
        print("13. Convert text to lowercase")
        print("14. Convert text to uppercase")
        print("15. Strip whitespace")
        print("16. Partition text based on separator")
        print("17. Replace substring")
        print("18. Reverse text (custom)")
        print("19. Swapcase")
        print("20. Title case text")
        print("21. Zero-fill text")
        print("22. Exit")
        
        choice = input("Enter your choice (1-22): ")
        
        if choice == "1":
            # Capitalize text
            print(f"Capitalized text: {text.capitalize()}")
        
        elif choice == "2":
            # Casefold text (for case-insensitive comparison)
            print(f"Casefolded text: {text.casefold()}")
        
        elif choice == "3":
            # Center the text with width 30 and '*' as the fill character
            print(f"Centered text: {text.center(30, '*')}")
        
        elif choice == "4":
            # Count occurrences of a substring
            substring = input("Enter the substring to count: ")
            print(f"Occurrences of '{substring}': {text.count(substring)}")
        
        elif choice == "5":
            # Check if text ends with a suffix
            suffix = input("Enter the suffix: ")
            print(f"Does text end with '{suffix}'? {text.endswith(suffix)}")
        
        elif choice == "6":
            # Check if text starts with a prefix
            prefix = input("Enter the prefix: ")
            print(f"Does text start with '{prefix}'? {text.startswith(prefix)}")
        
        elif choice == "7":
            # Expand tabs to spaces
            print(f"Text with expanded tabs: {text.expandtabs(4)}")
        
        elif choice == "8":
            # Find a substring
            substring = input("Enter the substring to find: ")
            print(f"First occurrence of '{substring}': {text.find(substring)}")
        
        elif choice == "9":
            # Get index of substring (raises error if not found)
            substring = input("Enter the substring to find: ")
            try:
                print(f"Index of '{substring}': {text.index(substring)}")
            except ValueError:
                print(f"'{substring}' not found in the text.")
        
        elif choice == "10":
            # Check if text is alphanumeric
            print(f"Is the text alphanumeric? {text.isalnum()}")
        
        elif choice == "11":
            # Check if text is alphabetic
            print(f"Is the text alphabetic? {text.isalpha()}")
        
        elif choice == "12":
            # Check if text is numeric
            print(f"Is the text numeric? {text.isdigit()}")
        
        elif choice == "13":
            # Convert text to lowercase
            print(f"Lowercase text: {text.lower()}")
        
        elif choice == "14":
            # Convert text to uppercase
            print(f"Uppercase text: {text.upper()}")
        
        elif choice == "15":
            # Strip whitespace from both ends
            print(f"Stripped text: {text.strip()}")
        
        elif choice == "16":
            # Partition text based on separator
            separator = input("Enter the separator to partition the text: ")
            print(f"Partitioned text: {text.partition(separator)}")
        
        elif choice == "17":
            # Replace substring
            old = input("Enter the word to replace: ")
            new = input("Enter the new word: ")
            print(f"Replaced text: {text.replace(old, new)}")
        
        elif choice == "18":
            # Reverse the text (custom method)
            print(f"Reversed text: {text[::-1]}")
        
        elif choice == "19":
            # Swap case (lowercase becomes uppercase and vice versa)
            print(f"Swapped case text: {text.swapcase()}")
        
        elif choice == "20":
            # Title case text
            print(f"Title case text: {text.title()}")
        
        elif choice == "21":
            # Zero-fill text (pad text with zeros on the left)
            width = int(input("Enter the width to zero-fill: "))
            print(f"Zero-filled text: {text.zfill(width)}")
        
        elif choice == "22":
            print("Exiting the Advanced Text Processor. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the advanced text processor
advanced_text_processor()
