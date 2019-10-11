from datetime import date 
  
def age(x): 
    today = date.today() 
    a = today.year - x.year - ((today.month, today.day) < (x.month, x.day)) 
    return a 
      
# Driver code  
print(age(date(1998, 12, 31)), "years") 
