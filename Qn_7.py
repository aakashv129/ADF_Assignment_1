name=input("Enter the name:")
age=int(input("Enter the age:"))
gender=input("Enter the gender:")
salary=int(input("Enter the salary:"))
state=input("Enter the state:")
city=input("Enter the city:")

class employee:
    name=""
    age=0
    gender=""
    salary=0
    state=""
    city=""

    def declareemployee(self,name,age,gender,salary,state,city):
        self.name=name
        self.age=age
        self.gender=gender
        self.salary=salary
        self.state=state
        self.city=city

    def printemployee(self):
        print("Name\t:",self.name)
        print("Age\t:",self.age)
        print("Gender\t:",self.gender)
        print("State\t:",self.state)
        print("city\t:",self.city)
        print("salary\t:",self.salary)

emp=employee()
emp.declareemployee(name,age,gender,salary,state,city)
emp.printemployee()