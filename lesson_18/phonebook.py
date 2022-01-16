import json

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

def add():
    name = input('Write your name: ')
    surname = input('Write your surname: ')
    full = input('Write your full name: ')
    phone = input('Write your phone: ')
    city = input('Write your city: ')
    new_dict = {'name': name, 'surname': surname, 'full_name': full, 'phone': phone, 'city': city}
    phonebook.append(new_dict)
    return phonebook


def search_name():
    name = input('What name you search?')
    for contact in phonebook:
        if contact['name'] == name:
            return contact
        return 'This name not found'


def search_lastname():
    surname = input('What surname you search?')
    for contact in phonebook:
        if contact['surname'] == surname:
            return contact
        return 'This surname not found'


def search_full():
    fullname = input('What fullname you search?')
    for contact in phonebook:
        if contact['full_name'] == fullname:
            return contact
        return 'This full name not found'


def phone():
    phone_search = input('What phone you search?')
    for contact in phonebook:
        if contact['phone'] == phone_search:
            return contact
        return 'This phone not found'


def delete_record():
    delete = input('What contact you want delete?')
    for contact in phonebook:
        if contact['name'] == delete:
            contact.clear()
    return phonebook

def print_phonebook():
    print(phonebook)