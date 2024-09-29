# Contacts Management System using Dictionary

contacts = {
    "John": {"phone": "123-456-7890", "email": "john@example.com"},
    "Alice": {"phone": "987-654-3210", "email": "alice@example.com"}
}

# Function to add a new contact
def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")

# Function to update an existing contact
def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")

# Function to search a contact
def search_contact(name):
    if name in contacts:
        print(f"Contact Found: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

# Function to list all contacts
def list_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")

# Menu for the Contact Management System
def contact_management_menu():
    while True:
        print("\nContact Management System")
        print("1. Add new contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. Search contact")
        print("5. List all contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            update_contact(name, phone if phone else None, email if email else None)

        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == '4':
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == '5':
            list_contacts()

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice, please try again.")

# Start the system
contact_management_menu()
