from collections import UserDict

class AddressBook(UserDict):
   
    def add_record(self, rec):
        key = rec.name.value
        self.data[key]=rec

class Record:

    def __init__(self, name: str, phone = None, email = None) -> None:
        self.name = Field(name)
        self.email = Field(email)
        self.phone = Phone(phone)

    def info(self):
        return {"name": self.name.value, "phone": self.phone.get_list()}

    def __str__(self):
        return f'{{"name": {self.name.value}, "phone": {self.phone.value}, "email": {self.email.value}}}'


class Field:
    def __init__(self, value: str) -> None:
        self.value = value
   

class Name:
    def __init__(self, value: str) -> None:
        self.name = Field(value)
       
class Address:
    def __init__(self, value: str) -> None:
        self.address = Field(value)

class Phone:
    
    def __init__(self, phones = None) -> None:
        self.value = list()
        if (phones):
            self.add(phones)

    def add(self, phones) -> None:
        if (phones):
            if (isinstance(phones, list)):
                for phone in phones:
                    self.value.append(phone)
            else:
                self.value.append(phones)

    def remove(self, phone: str) -> None:
        self.value.remove(phone)


    def get_list(self) -> list:
        return self.value

    def __repr__(self) -> list:
        return self.value

    def __str__(self) -> str:
        return ",".join(self.value)


ab = AddressBook()
rec = Record("Jon1",["000-0001","000-0002"])
rec.phone.add("000-0003")
print(rec)

ab.add_record(rec)
rec = Record("Jon2", ["200-0001", "200-0002"])
ab.add_record(rec)
rec = Record("Jon3", "300-0001", "email3")
ab.add_record(rec)


for k,v in ab.items():
    print(k, v)
