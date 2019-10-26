a=int(input("enter 1st number"))
one=a
b=int(input("enter 2nd number"))
two=b

def odd(one,two):
	newlist = []
	for i in range(one,two):
		if i%2 !=0:
			newlist.append(i)
	print(newlist)
	return newlist
	
odd(one,two)

#alternate way
def oddRange(num1, num2):
	for i in range(num1+1, num2):
		if i%2 != 0:
			print(i)

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
oddRange(num1, num2)
