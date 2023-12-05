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
        new_l = []
        for i in filter(lambda x:x.value !=phone, self.phones):
            new_l.append(i)
        self.phones = new_l
        
    def edit_phone(self,phone, new_phone):
        for i in self.phones:
            if(i.value == phone):
                i.value = new_phone
        
    def find_phone(self,phone):
        search_v = {}
        for i in filter(lambda x:x.value ==phone, self.phones):
            search_v = i
        return search_v
        
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self,user):
        phones = []
        for p in user.phones:
            phones.append(p.value)
            print(p.value)
        
        # self.data.update({user.name.value : phones})
        self.data.update(user)
        
    def find(self,name):
        print(self.data[name])
        # user = {}
        # for i in filter(lambda x:x[name] ==name, self.data):
        #     user = i
        return True
    def delete(self,name):
        new_l ={}
        for i in filter(lambda x:x[name] !=name, self.data):
            new_l.update(i)
        self.data = new_l
        
    
book = AddressBook()
kari_record = Record('Kari')
kari_record.add_phone('1309198934')
kari_record.add_phone('0909202003')
book.add_record(kari_record)

platon_record = Record('Platon')
platon_record.add_phone('7894561230')
platon_record.add_phone('0123654789')
book.add_record(platon_record)

# kari = book.find('Kari')

print(book.data)

# for name,record in book.data.items():
#     print(record, 'here')
#     print(name, 'here')
    

