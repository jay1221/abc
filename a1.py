#task1
import copy

list1 = ["jay",1998,"blore"]

# Length of the list
print("length of list = ",len(list1))

# Create a new list as an element of an existing list
blore = ["india",21,"dec"]

# using slice operator
print("my list :",list1)
print(list1[2:])

# Replace second element with a fruit name
list1[1]="orange"
print("changed list :",list1)

list2=["aaa",123]
print("list 2 :",list2)

# Concatenating two lists
list3=list1+list2
print("concatenated list :",list3)

# 2 ways to clone a list
list4=list3[ : ]
print(list4)

list5=copy.copy(list1)
print(list5)

# Split a list into evenly sized chunks
print("\nAfter splitting into groups of 3: ")
for i in range(0, len(list1), 3):
    print(list1[i:i+3])

#task2
# 2) Create a tuple with numbers and print one item
tuple1=(111,222,333)
print(tuple1) 

print(tuple1[0])

#task3
# 3) Converting tuple to list
list9=list(tuple1)
print(list9)

