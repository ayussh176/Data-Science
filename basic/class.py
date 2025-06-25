class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def display(self):
        print("ID:",self.id,"name:",self.name)

emp = Employee(1,"ayush")
emp.display()

del emp.id #del is use to delete the instance or complete object

try:
    print(emp.id)
except Exception as e:
    print("id is not found")

del emp

try:
    print(emp.name)
except Exception as e:
    print("employee not found")