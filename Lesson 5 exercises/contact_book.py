# Practical Task
# Task Overview

# Build a command-line contact book called contact_book.py that stores contacts as a list of dictionaries and allows the user to add, search, view, and delete contacts. This is a foundational data structure pattern used in virtually every real app.

# Requirements

# Store contacts as a list of dictionaries, each with keys: name, phone, email
# Implement an add_contact() function that appends a new dictionary to the list
# Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)
# Implement a delete_contact(name) function that removes a contact by name
# Implement a view_all() function that displays all contacts in a formatted layout
# Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)
 

# Outcome of Task

# At the end of this task, you should be competent in creating and manipulating lists and dictionaries, using common methods to access and modify data, explaining the difference between mutable and immutable data types, building lists of dictionaries to represent structured collections of real-world data, and iterating over lists and dictionaries using for loops. Before progressing to the next unit, complete the Unit 4 Quiz to check your understanding of the key concepts covered, identify any areas that may need further practice, and reinforce your learning.  

# I need to make a contact book the allows a user to add name phone and email


contacts = []   # global list to store contacts

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"Contact '{name}' added successfully!\n")

def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def delete_contact(name):
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            removed = contacts.pop(i)
            print(f"Contact '{removed['name']}' deleted.\n")
            return
    print(f"No contact found with the name '{name}'.\n")

def view_all():
    if not contacts:
        print("No contacts to display.\n")
        return
    print("\n--- All Contacts ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}\n")

def main():
    while True:
        print("===== Contact Manager =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            name = input("Enter name to search: ").strip()
            result = search_contact(name)
            if result:
                print(f"Found: Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}\n")
            else:
                print(f"No contact found with the name '{name}'.\n")
        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            delete_contact(name)
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")

# Run the program
if __name__ == "__main__":
    main()


 