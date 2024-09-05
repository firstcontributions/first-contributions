def pelindrome(num):
    num_str= str(num)
    
    result= int(num_str[::-1])
    return result
    
number= int(input("Enter your number: ")) 

result= pelindrome(number)

if number==result:
    print("Pelindrome")
    
else:
    print("Not Pelindrome")    

  