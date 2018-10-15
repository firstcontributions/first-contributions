#Hactoberfest


n=int(input())
l=list(map(int,input().split()))
for i in range (1,n+1):
    for j in range (0,n):
        if l[j]==i:
            r=j+1
            for k in range (0,n):
                if l[k]==r:
                    print(k+1)
                    break
