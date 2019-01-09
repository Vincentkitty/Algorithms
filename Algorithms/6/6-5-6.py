def heap_increase_key(A, i, key):
    if key < A[i]:
        return "new key smaller than current key"
    A[i] = key
    while i > 1 and key > A[i / 2]:
        A[i]=A[i / 2]
        i /= 2
    A[i]=key