t=int(input())
while t>0:
    n=int(input())
    if n<4:
        print(-1)
    elif n==4:
        print(2,4,1,3)
    else:
        for i in range(1,n+1,2):
            print(i,end=" ")
        for i in range(2,n+1,2):
            print(i,end=" ")
        print(end="\n")
    t-=1
