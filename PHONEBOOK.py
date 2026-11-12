phonebook = {}

while True:
    print('1-> Add Contact\n 2-> Search Contact\n3-> Update Contact\n4-> Delete Contact\n5-> Display All Contacts\n6-> Exit')
    n = int(input('Enter the choice: '))
    if n == 1:
        name = input('Enter name: ')
        phone = input('Enter phone number: ')
        phonebook[name] = phone
        print('Contact added successfully')
    elif n == 2:
        name = input('Enter name: ')
        if name in phonebook:
            print('Phone Number:', phonebook[name])
        else:
            print('Contact not found')
    elif n == 3:
        name = input('Enter name: ')
        if name in phonebook:
            phone = input('Enter new phone number: ')
            phonebook[name] = phone
            print('Contact updated successfully')
        else:
            print('Contact not found')
    elif n == 4:
        name = input('Enter name: ')
        if name in phonebook:
            del phonebook[name]
            print('Contact deleted successfully')
        else:
            print('Contact not found')
    elif n == 5:
        for name, phone in phonebook.items():
            print(name, ':', phone)
    elif n == 6:
        break
    else:
        print('Invalid choice')