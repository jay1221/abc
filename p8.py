#temperature converter python pgm that is menu driven

def ():
	t=tuple()	
	
	

def temp():
	print("1:C to F,2:F to C,3:finish");
	x=input("1:C to F,2:F to C,3:finish");
	
	if(x==1)
	{
		print("enter celcius")
		c=input()
		f = (9/5)*c+32
		print("f= ",f)
	}
	 else if(x==2)
	 {
	 	print("enter fahrenheit")
	 	f=input()
	 	c = (f-32)*(5/9)
	 	print("c= ",c)
	 }
	 else if(x==3)
	 {
	 	print("finish")
	 }
	 else
	 {
	 	print("invalid")
	 }
