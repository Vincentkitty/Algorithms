def min_heapify(A,i):  #A.size()=n+1
    if(2*i>A.size()-1):
        return
    l=2*i
    r=2*i+1
    if A[l]<A[i]:
        minest=l
    else:
        minest=i
    if A[minest]>A[r]:
        minest=r
    A[minest],A[i]=A[i],A[minest]
    min_heapify(A,minest)


