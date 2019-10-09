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

