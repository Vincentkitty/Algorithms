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
        if A[j]>x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1
