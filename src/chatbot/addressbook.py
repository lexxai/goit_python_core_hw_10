from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, rec):
        key = rec.name.value
        self.data[key] = rec
    
    def get_record(self, key):
        return self.data[key]

    def remove_record(self, key):
        del self.data[key]

class Field:

    def __init__(self, value: str) -> None:
        self.value = value

    def __eq__(self, other):
        return self.value == other

    def __repr__(self):
        return self.value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    ...


class Address(Field):
    ...


class Email(Field):

    def __init__(self, value: str) -> None:
        if not (value and '@' in value):
            value = None
        super().__init__(value)


class Phone(Field):
    ...


class Record:

    def __init__(self, name: Name, phone: Phone = None,
                 email: Email = None, address: Address = None) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phones = []
        self.add_phone(phone)

    def add(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.add_phone(field)
            
    def remove(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.remove_phone(field)
   
    def add_phone(self, phone: Phone) -> None:
        if (phone):
            #phones_value = [i.value for i in self.phones]
            if (isinstance(phone, list)):
                for ph in phone:
                    if ph not in self.phones:
                        self.phones.append(ph)
            elif phone not in self.phones:
                self.phones.append(phone)
            return True
            
    def change_phone(self, old_phone: Phone, new_phone: Phone) -> None:
        if old_phone and new_phone:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)

    def remove_phone(self, phone: Phone) -> None:
        self.phones.remove(phone)
        return True

    def get_phones(self) -> str:
        return ";".join([ str(ph) for ph in self.phones])

    def __str__(self) -> str:
        return f'name: {self.name}, phone: {self.get_phones()}, '\
            f'email: {self.email}, address: {self.address}'
