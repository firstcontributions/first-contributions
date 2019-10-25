def partition(a,p,r): 
    i = ( p-1 )
    pivot = a[r]
    for j in range(p,r):
        if   a[j] < pivot: 
            i = i+1 
            a[i],a[j] = a[j],a[i] 
    a[i+1],a[r] = a[r],a[i+1] 
    return ( i+1 ) 

def QuickSort(a,p,r) : // Python Implementation Of QuickSort
if(p<r) :
    q = Partition(a,p,r)
    x = QuickSort(a,p,q-1)
    x = QuickSort(a,q+1,r)
  return 
    
def QuickSearch(a,p,r,k,sorted) :
  x = -1 
  if(sorted) :
    return BinarySearch(a) 
  if(p<r) :
    q = Partition(a,p,r)
    if a[q] == k :
      return q 
    else if a[q] > k :
      return QuickSearch(a,p,q-1,k,sorted)
    else :
      return QuickSearch(a,q+1,r,k,sorted)
  return x

"""
Usage Of 
QuickSearch(a,p,r,k,sorted) :

a      : Array 
p      : Starting Index
r      : Ending Index
k      : Element To Be Searched
sorted : Variable to show whether an array is sorted 

sorted will be set to True when One of the search returns -1 
"""
