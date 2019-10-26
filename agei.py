from datetime import date

def age(x):
	a=2019-x
	return a
dob=input("enter ur dob [dd-mm-yyyy] ")
x=int(dob[6:])
age(x)
print("your age is "+str(age(x))) 
