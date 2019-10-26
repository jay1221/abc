#task1

# i)Create class having attributes name, age and marks of 3 subjects
class student:  
    # ii) Create a constructor accepting the values
    def __init__(self,name,age,m)
        self.name=name;
        self.age=age;
        self.m=m[ : ]  
        
    # iii) Member function to display the details
    def display(self):
        print("name= ",self.name)
        print("age= ",self.age)
        i = 1
        for mark in self.m:
            print("mark ", i," = ",mark)
            i=i+1    
            
# iv) Ask user for the inputs
m = []
def accept():
    name=input("enter name of student: ")
    age=input("enter age of student: ")
    print("enter 3 marks")
    for i in range(3):
        m.append(input())
    return name,age,m

name,age,m = accept()
s1 = student(name,age,m)

m = []
name,age,m = accept()
s2 = student(name,age,m)
  
# v) calling display function  
print(s1.display())
print()
print(s2.display())

#task2
# Create a dictionary to hold student details with Register numbers and print details of students with even register number

Sdetails = {
    10: {
        "name": "sanj",
        "age": 20,
        "sec": "C"
    },
    11: {
        "name": "nive",
        "age": 20,
        "sec": "A"
    },
    12: {
        "name": "neha",
        "age": 21,
        "sec": "B"
    },
    13: {
        "name": "vish",
        "age": 20,
        "sec": "C"
    },
    14: {
        "name": "trivi",
        "age": 20,
        "sec": "C"
    }
}

for i in Sdetails:
    if i % 2 == 0:
        print(i, " : ", Sdetails[i])
    
