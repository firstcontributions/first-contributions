def BinarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid = (si+ei)//2
    if a[mid] == x:
        return mid
    elif a[mid]>x:
        return BinarySearch(a,x,si,mid-1)
    else:
        return BinarySearch(a,x,mid+1,ei)
print(BinarySearch([1,2,3,4,5,6],3,0,5))
