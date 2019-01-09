def max_heapify(A,i): # A.size()=n+1
    while 2*i<=A.size()-1:
        if A[2*i]>A[i]:
            largest=2*i
        else:
            largest=i
        if A[2*i+1]>A[largest]:
            largest=2*i+1
        A[largest],A[i]=A[i],A[largest]
        i=largest
        
def heap_delete(A,i): #A.size=n+1
    A[i]=A[A.size-1]
    A.size-=1
    max_heapify(A,i)