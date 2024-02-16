import os


class Contact:
    def __init__(self, name, phone, email, note, id=None):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__note = note
        self.__id = id

    def __str__(self):
        return f"{self.__name}\t{self.__phone}\t{self.__email}\t{self.__note}"

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email

    @property
    def note(self):
        return self.__note

    def maybe_iam(self, mask, key='name'):
        return ((key == 'name' and mask in self.name) or (key == 'phone' and mask in self.phone)
                or (key == 'email' and mask in self.email) or (key == 'note' and mask in self.note))

    def edit(self, amount, key='name'):
        if key == 'name':
            self.__name = amount
        elif key == 'phone':
            self.__phone = amount
        elif key == 'email':
            self.__email = amount
        elif key == 'note':
            self.__note = amount
        else:
            raise ValueError


class Book:
    def __init__(self, path):
        self.__updated = False
        self.__read_file(path)
        self.__name = path

    def __str__(self):
        return '\n'.join([str(contact) for contact in self.__content])

    def __read_file(self, path):
        try:
            content = []
            with open(path, 'r', encoding='utf-8') as file:
                id = 1
                for line in file:
                    name, phone, email, note = line.split('\t')
                    content.append(Contact(name, phone, email, note, id))
                    id += 1
            self.__content = content
        except FileNotFoundError:
            self.__create_file(path)
            self.__read_file(path)

    def __write_file(self, path):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(str(self))

    def __create_file(self, path):
        os.open(path, os.O_CREAT)

    @property
    def name(self):
        return self.__name

    @property
    def have_changes(self):
        return self.__updated

    def add(self, contact):
        self.__content.append(contact)
        self.__updated = True

    def find(self, mask, key='name'):
        return '\n'.join(str(contact) for contact in self.__content if contact.maybe_iam(mask, key))

    def change(self, name, contact):
        pass

    def save(self):
        self.__write_file(self.name)
        self.__updated = False


class Menu:
    def __init__(self, initial):
        lines = initial.split('\n')
        self.__content = {line.split('-')[0].rstrip(' '): line.split('-')[1].lstrip(' ') for line in lines}
        print(self.__content)

    def __str__(self):
        return '\n'.join([f'{key} - {self.__content[key]}' for key in self.__content.keys()])

    def is_esists(self, key):
        return True if key in self.__content.keys() else False

    def show(self):
        print(self)
