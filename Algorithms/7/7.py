import  random
def quick_sort(A,p,r):
    if p<=r:
        q=Partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
    return

def Partition(A,p,r):
    i=p-1
    x=A[r]
    for j in range(p,r):
        if A[j]<x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def random_quick_sorter(A,p,r):
    if p<=r:
        q=random_partition(A,p,r)
        random_quick_sorter(A,p,q-1)
        random_quick_sorter(A,q+1,r)
    return
def random_partition(A,p,r):
    i=random.random(p,r)
    A[i],A[r]=A[r],A[i]
    return Partition(A,p,r)