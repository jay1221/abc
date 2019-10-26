students = { "1ms16is100":"asha","1ms16is101":"ashok","1ms16is102":"rekha","1ms16is103":"suma"}
list = ["value1","value2","value3","value3","value4"]
list2 = []
j=0

#print the student details
for i in students:
	print ("key is",i,"value is",students[i])
	list[j]=students[i]
	#list2[j]=i
	j=j+1
print(list)

#print(list2)
print (students.keys())
print (students.values())
print (students.items())
