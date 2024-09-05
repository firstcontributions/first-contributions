def is_armstrong(num):
    num_str= str(num)
    num_digits= len(num_str)
    print(num_digits)
    sum_power=0
    for digits in num_str:
        sum_power= sum_power + int(digits)**num_digits
    return sum_power  
    
    
  
n= int(input("Enter a number: "))
p=is_armstrong(n) 
if n==p:
    print("Armstrong")
    
else:
    print("Not Armstromg")    
    