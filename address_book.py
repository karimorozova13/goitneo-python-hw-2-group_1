from collections import UserDict

class Field:
    def __init__(self,val):
        self.value = val
    def __str__(self) -> str:
        return str(self.value)
    
class Name(Field):
    def __init__(self,name) -> None:
        super().__init__(name)
        
class Phone(Field):
    def __init__(self, val) -> None:
        super().__init__(val)
        if not self.is_valid_phone():
            raise ValueError("Invalid phone number")
    def is_valid_phone(self):
        return len(str(self.value)) == 10
    
class Record:
    def __init__(self,name) -> None:
        self.name = Name(name)
        self.phones =[]
        
    def add_phone(self,phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self,phone):
        self.phones = [p for p in self.phones if p.value != phone]
        
    def edit_phone(self,phone, new_phone):
        for i in self.phones:
            if(i.value == phone):
                i.value = new_phone
                break
        
    def find_phone(self,phone):
        return next((p for p in self.phones if p.value == phone), None)
    
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self,user):
       self.data[user.name.value] = user
        
    def find(self,name):
        return self.data[name] if name in self.data.keys() else None
    def delete(self,name):
        if name in self.data:
            del self.data[name]
        
    
book = AddressBook()
kari_record = Record('Kari')
kari_record.add_phone('1309198934')
kari_record.add_phone('0909202003')
kari_record.edit_phone('0909202003', '1313131313')

book.add_record(kari_record)

platon_record = Record('Platon')
platon_record.add_phone('7894561230')
platon_record.add_phone('0123654789')
book.add_record(platon_record)

kari = book.find('Kari')
book.delete('Platon')
search =kari_record.find_phone('0909202003')

for name,record in book.data.items():
    print(record)
    

