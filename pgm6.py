#demo:classes in python
#concept:use of del function to attribute of obj and obj itself
class Person:
	def __init__(self,name,age):#constructor of class
		self.name=name;
		self.age= age

p1=Person("Suppandi",14)

print("\nName of person #1 is",p1.name)
print("\nAge of person #1 is",p1.age)

print("\n *** printing after deleting age attribute for p1 ***")
del p1.age# deleting age attribute

print("\nName of person #1 is",p1.name)
#print("\nAge of person #1 is",p1.age)

print("\n *** printing after deleting p1 ***")
del p1

#print("\n name of person #1 is",p1.name)
