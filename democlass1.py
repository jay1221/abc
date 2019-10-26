#Demo: Classes in python

class Person:
	def __init__(self,name,age):		#Constructor of the class Person
		self.name=name;
		self.age= age

#2 objs p1 and p2 are created,the __init__ constructor is automatically called 
p1=Person("Suppandi",14)
p2=Person("Ramu",12)

print("\nName of person #1 is",p1.name)
print("\nAge of person #1 is",p1.age)

print("\nName of person #2 is",p2.name)
print("\nAge of person #2 is",p2.age)

p2.age=10	#Attributes of the objects can be modified. By default public

print("\nmodified age of person #2 is",p2.age)

