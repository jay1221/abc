x = 0

if x > 0.0:
	print ("positive")
elif x <0.0:
	print("negative")
	x=-1.0*x
else:
	print("zero")

	
#Alternative way
if x > 0:
	print("+ve")
else:
	if x < 0:
		print("-ve")
		x = -1.0*x
	else:
		print("0")
