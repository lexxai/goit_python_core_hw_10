# goit_python_core_hw_10

## test
### input
```
    ab = AddressBook()
    rec = Record("Jon1",["000-0001","000-0002"])
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

    for k,v in ab.items():
        print(k, v)
```

### result
```
Jon1 "name": Jon1, "phone": 000-0002;000-0003, "email": None, "address": Jon1 Home Street
Jon2 "name": Jon2, "phone": 200-0001;200-0002, "email": Jon2@email.com, "address": None
Jon3 "name": Jon3, "phone": 300-0001, "email": Jon3@email.com, "address": None
```
