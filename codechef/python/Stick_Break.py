t=int(input())
while t>0:
    l,k=map(int,input().split())
    if l%k:
        print(1)
    else:
        print(0)
    t-=1
