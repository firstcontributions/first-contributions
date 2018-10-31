 take=list() 
 for _ in range(int(input("number of students:"))): 
          name = input("Enter name:") 
          score = float(input("Enter marks:")) 
          take_=list() 
          take_.append(name) 
          take_.append(score) 
  
 
          take.append(take_) 
  
 
  
 
  take=sorted([(v,k) for (k,v) in take]) 
  take1=take[1] 
  print(take1[1]) 
  print(take1[0]) 
