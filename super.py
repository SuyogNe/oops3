class Person(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def display(self):
        print(self.name)
        print(self.age)

class Employee(Person):
    def __init__(self,address,id,name,age):
        super().__init__(name,age)
        self.address=address
        self.id=id
    
    def ent(self):
        print(self.address)
        print(self.id)
        
    
        
e1=Employee("Bangalore",101,"John",22)
e1.display()
e1.ent()

