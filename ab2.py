from datetime import date

def ageconverter(num):
	age=2019-num
	return age
dob=input("enter ur dob [dd-mm-yyyy] ")
y=dob[6:]
num=int(y)
output=ageconverter(num)
print("your age is "+str(output)) 
