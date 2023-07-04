from collections import UserDict

class AddressBook(UserDict):
   
    def add_record(self, rec):
        key = rec.name.value
        self.data[key]=rec

class Record:

    def __init__(self, name: str, phone=None, email=None, address=None) -> None:
        self.name = Name(name)
        self.email = Email(email)
        self.address = Address(address)
        self.phone = []
        self.add_phone(phone)
        
    def add_phone(self, phone: str) -> None:
        if (phone):
            if (isinstance(phone, list)):
                self.phone.extend(phone)
            else:
                self.phone.append(phone)

    def remove_phone(self, phone: str) -> None:
        if phone in self.phone:
            self.phone.remove(phone)

    def get_phones(self) -> str:
        return ";".join(self.phone)

    def __str__(self):
        return  f'name: {self.name}, phone: {self.get_phones()}, '\
                f'email: {self.email}, address: {self.address}'


class Field:
    
    def __init__(self, value: str) -> None:
        self.value = value
    
    def __str__(self):
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


if __name__ == "__main__":
    ab = AddressBook()
    rec = Record("Jon1",["000-0001","000-0002"],email="bademail")
    rec.add_phone("000-0003")
    #rec.remove_phone("000-0001")
    #print(rec)

    ab.add_record(rec)
    rec = Record("Jon2", ["200-0001", "200-0002"])
    ab.add_record(rec)
    rec = Record("Jon3", "300-0001", "Jon3@email.com")
    ab.add_record(rec)

    ab['Jon1'].remove_phone("000-0001")
    ab['Jon1'].address.value="Jon1 Home Street"
    ab['Jon2'].email.value = "Jon2@email.com"

    for v in ab.values():
        print( v)
