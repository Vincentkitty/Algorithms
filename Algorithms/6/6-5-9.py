def heap_merge_k(A,k): #A is a tuple consist of heap which num is k
    n=sum(A[i].size()-1 for i in range(A.size))
    res=[A[0]]
    for i in A[1:]:
        for j in i:
           heap_increase_key(res,j)
