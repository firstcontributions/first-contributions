print("Enter N")
n=int(input())
flag=0
flag1=0
num=[]
for i in range(n):
    num.append(int(input()))
dic={}
for i in num:
    try:
        dic[i]+=1
    except:
        dic[i]=1

for key, value in dic.items():
    if(value!=1):
        if(flag==0):
            print("Duplicate Numbers")
            flag=flag+1
        print(key)
    else:
        if(flag1==0):
            print("Non Duplicate Numbers")
            flag1=flag1+1
        print(key)
