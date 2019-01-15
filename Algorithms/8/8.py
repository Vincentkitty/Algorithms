def counting_sort(A,k):
    c=[0]*(k+1)
    B=[0]*A.__len__()
    for i in A:
        c[i]+=1
    for i in range(1,k+1):
        c[i]+=c[i-1]
    for i in A[::-1]:
      B[c[i]-1]=i
      c[i]-=1
    return B

# A=[2,5,3,0,2,3,0,3]
# print(counting_sort(A,5))
