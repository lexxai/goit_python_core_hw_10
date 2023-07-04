from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, rec):
        key = rec.name.value
        self.data[key] = rec
    
    def get_record(self, key):
        return self.data[key]

    def remove_record(self, key):
        if key in self.data:
            del self.data[key]

class Field:

    def __init__(self, value: str) -> None:
        self.value = value

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
        self.phone = []
        self.add_phone(phone)

    def add(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.add_phone(field)
            
    def remove(self, field: Field) -> bool:
        if isinstance(field, Phone):
            return self.remove_phone(field)
   
    def add_phone(self, phone: Phone) -> None:
        if (phone):
            if (isinstance(phone, list)):
                self.phone.extend(phone)
            else:
                self.phone.append(phone)
            return True
            
    def change_phone(self, phone: Phone) -> None:
        if (phone):
            self.phone.clear()
            self.add_phone(phone)

    def remove_phone(self, phone: Phone) -> None:
        if phone in self.phone:
            self.phone.remove(phone)
            return True

    def get_phones(self) -> str:
        return ";".join([ str(ph) for ph in self.phone])

    def __str__(self) -> str:
        return f'name: {self.name}, phone: {self.get_phones()}, '\
            f'email: {self.email}, address: {self.address}'

