def main():
    phonebook = {"Alice": "123-456-7890", "Bob": "987-654-3210", "Charlie": "555-555-5555" }
    phonebook["Alice"] = "111-222-3333"
    phonebook.pop("Bob")
    for name, number in phonebook.items():
        print(name, ":", number)





main()
