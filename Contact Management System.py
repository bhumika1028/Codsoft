# Contact Management System

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter home address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"\nContact '{name}' added successfully!\n")

def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("\nNo contacts available.\n")

def search_contact():
    search_term = input("Enter name or phone number to search: ").lower()
    found = False
    for name, details in contacts.items():
        if search_term in name.lower() or search_term in details['phone']:
            print(f"\nFound Contact - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("\nNo contact found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"\nCurrent details of '{name}':")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        
        print("\nEnter new details (leave blank to keep current value):")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new home address: ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print(f"\nContact '{name}' updated successfully!\n")
    else:
        print("\nContact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"\nContact '{name}' deleted successfully!\n")
    else:
        print("\nContact not found.\n")

def main_menu():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
