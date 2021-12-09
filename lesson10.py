import json

if __name__ == '__main__':

    # task 1
    with open('myfile.txt', 'w') as f:
        f.write('Hello file world!')

    with open('myfile.txt', 'r') as text:
        text = text.readline()
    print(text)

    # task 2
    phonebook = [
        {'name': 'Tanya',
         'surname': 'Solona',
         'full_name': 'Tanya Solona',
         'phone': '0633288000',
         'city': 'Kyiv'},
        {'name': 'Ann',
         'surname': 'Ivanova',
         'full_name': 'Ann Ivanova',
         'phone': '0964448000',
         'city': 'Kyiv'},
        {'name': 'Dmytro',
         'surname': 'Ignatov',
         'full_name': 'Dmytro Ignatov',
         'phone': '0665558000',
         'city': 'Kyiv'}

    ]

    with open('phonebook.json', 'w') as file_object:
        json.dump(phonebook, file_object)

    def add(new):
        name = input('Write your name: ')
        surname = input('Write your surname: ')
        full = input('Write your full name: ')
        phone = input('Write your phone: ')
        city = input('Write your city: ')
        new_dict = {'name': name, 'surname': surname, 'full_name': full, 'phone': phone, 'city': city}
        new.append(new_dict)
        print(new)

    def search_name(name):
        for contact in phonebook:
            if contact['name'] == name:
                print(contact)
            else:
                print('This name not found')

    def search_lastname(surname):
        for contact in phonebook:
            if contact['surname'] == surname:
                print(contact)
            else:
                print('This surname not found')

    def search_full(fullname):
        for contact in phonebook:
            if contact['full_name'] == fullname:
                print(contact)
            else:
                print('This full name not found')

    def phone(phone_search):
        for contact in phonebook:
            if contact['phone'] == phone_search:
                print(contact)
            else:
                print('This phone not found')


    def delete_record(delete):
        for contact in phonebook:
            if contact['name'] == delete:
                contact.clear()
        print(phonebook)

    a = input('search by name - "1", by lastname - "2", by fullname - "3", by phone - "4", for delete contact - "5"'
              'for add - "6"')

    while a != 'q':
        if a == '1':
            name = input('Write name for search: ')
            search_name(name)
        elif a == '2':
            surname = input('Write surname for search: ')
            search_lastname(surname)
        elif a == '3':
            fullname = input('Write full name for search: ')
            search_full(fullname)
        elif a == '4':
            phone_search = input('Write phone for search: ')
            phone(phone_search)
        elif a == '5':
            delete = input('Write name for delete:')
            delete_record(delete)
        elif a == '6':
            add(a)
            break
