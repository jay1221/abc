#task1
import copy
list1 = ["jay",1998,"blore"]
print("length of list = ",len(list1))

blore = ["india",21,"dec"]

print("my list :",list1)
print(list1[2:])

list1[1]="orange"
print("changed list :",list1)

list2=["aaa",123]
print("list 2 :",list2)

list3=list1+list2
print("concatenated list :",list3)

list4=list3[ : ]
print(list4)


list5=copy.copy(list1)
print(list5)

#task2
tuple1=(111,222,333)
print(tuple1) 

print(tuple1[0])

#task3
list9=list(tuple1)
print(list9)
