#A
#python pgm to read a list of ele
#create a new list that holds all the elements minus the duplicates(use functions)
def dup(l1):
	l2 = []
	for n in l1:
		if n not in l2:
			l2.append(n)				
	print(l2);
	return l2
l1=[1,2,3,4,5,5,5,6,3,2]
dup(l1);		

#2nd way for reference
def dup(l1):
	l2 = []
	for n in l1:
		if n not in l2:
			l2.append(n)		
	print(l2);
	return l2

dup([1,2,3,4,5,5,5,6,3,2]);		

#read list of numbers
#use one line comprehensions of create a new list of even nums
#reverse the list
s = [x**2 for x in range(10)] #read ele to list
m = [x for x in s if x % 2 == 0]
m.reverse()
print(s);
print(m);

#B
#write a python pgm to count frequency of words in a given file
from collections import Counter
def keep_counting(fname):
	with open(fname) as f:
		return Counter(f.read().split())
print("number of words in a file:",keep_counting("song.txt"))
