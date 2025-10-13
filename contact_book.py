import json
import os

FILE_NAME = 'contacts.json'

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as f:
        json.dump(contacts, f, indent=4)
        
def create_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully.")
    
def read_contact(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for name, info in contacts.items():
        print(f"nName: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print(f"  Address: {info['address']}")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print("Leave field empty to keep current value.")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ").strip()
    email = input(f"Enter new email address (current: {contacts[name]['email']}): ").strip()
    address = input(f"Enter new address (current: {contacts[name]['address']}): ").strip()
    
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address
    print(f"\nContact {name} updated successfully.")
    
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    del contacts[name]
    print(f"Contact {name} deleted successfully.")
    
def search_contact(contacts):
    name = input("Enter the name of the contact to search: ").strip().lower()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print(f"  Address: {info['address']}")
    else:
        print("Contact not found.")
        
def main():
    contacts = load_contacts()
    while True:
        print("\n-----Contact Book Menu-----")
        print("1. Create Contact")
        print("2. View all Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            create_contact(contacts)
        elif choice == '2':
            read_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            search_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            print("Goodbye!👍")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()