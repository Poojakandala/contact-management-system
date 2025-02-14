# list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("✅ Contact added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts found!\n")
        return
    print("\n📒 Contact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

# Function to search for a contact by name
def search_contact():
    search_name = input("🔍 Enter name to search: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"\n✅ Contact Found: {contact}")
            found = True
            break
    if not found:
        print("❌ Contact not found!\n")

# Function to update a contact
def update_contact():
    search_name = input("✏️ Enter name to update: ")
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            contact['phone'] = input("Enter new phone: ")
            contact['email'] = input("Enter new email: ")
            print("✅ Contact updated successfully!\n")
            return
    print("❌ Contact not found!\n")
# Function to delete a contact
def delete_contact():
    search_name = input("🗑️ Enter name to delete: ")
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            contacts.remove(contact)
            print("✅ Contact deleted successfully!\n")
            return
    print("❌ Contact not found!\n")

# Main 
while True:
    print("📱 Contact Management System")
    print("1️⃣ Add Contact")
    print("2️⃣ View Contacts")
    print("3️⃣ Search Contact")
    print("4️⃣ Update Contact")
    print("5️⃣ Delete Contact")
    print("6️⃣ Exit")
    
    choice = input("Enter your choice: ")

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
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.\n")