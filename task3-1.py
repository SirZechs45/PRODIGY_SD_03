import tkinter as tk
from tkinter import messagebox, simpledialog

def save_contacts_to_file():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact['Name']}|{contact['Phone']}|{contact['Email']}\n")
    

def load_contacts_from_file():
    contacts = []
    try:
        with open("contacts.txt", "r") as file:
            for line in file.readlines():
                name, phone, email = line.strip().split("|")
                contacts.append({"Name": name, "Phone": phone, "Email": email})
    except FileNotFoundError:
        pass
    return contacts


def add_contact(name, phone, email):
    contact = {"Name": name, "Phone": phone, "Email": email}
    contacts.append(contact)
    save_contacts_to_file()
    messagebox.showinfo("Success", "Contact added successfully!")

def view_contacts():
    contacts_str = "\n".join([f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}" for contact in contacts])
    messagebox.showinfo("Contacts", contacts_str)

def edit_contact(index, name, phone, email):
    if index is None:
        messagebox.showinfo("Info", "No index entered.")
        return
    if 0 <= index < len(contacts):
        contacts[index]["Name"] = name
        contacts[index]["Phone"] = phone
        contacts[index]["Email"] = email
        save_contacts_to_file()
        messagebox.showinfo("Success", "Contact edited successfully!")
    else:
        messagebox.showerror("Error", "Invalid index.")

def delete_contact(index):
    if index is None:
        messagebox.showinfo("Info", "No index entered.")
        return
    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        save_contacts_to_file()
        messagebox.showinfo("Success", f"Contact '{deleted_contact['Name']}' deleted successfully!")
    else:
        messagebox.showerror("Error", "Invalid index.")

def main():
    global contacts
    contacts = load_contacts_from_file()

    root = tk.Tk()
    root.title("Contact Management System")

    name_label = tk.Label(root, text="Name")
    name_label.pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    phone_label = tk.Label(root, text="Phone")
    phone_label.pack()
    phone_entry = tk.Entry(root)
    phone_entry.pack()

    email_label = tk.Label(root, text="Email")
    email_label.pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    add_button = tk.Button(root, text="Add Contact", command=lambda: add_contact(name_entry.get(), phone_entry.get(), email_entry.get()))
    add_button.pack()

    view_button = tk.Button(root, text="View Contacts", command=view_contacts)
    view_button.pack()

    edit_button = tk.Button(root, text="Edit Contact", command=lambda: edit_contact(simpledialog.askinteger("Input", "Enter the index of the contact to edit:"), name_entry.get(), phone_entry.get(), email_entry.get()))
    edit_button.pack()

    delete_button = tk.Button(root, text="Delete Contact", command=lambda: delete_contact(simpledialog.askinteger("Input", "Enter the index of the contact to delete:")))
    delete_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
