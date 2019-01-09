def max_heapify(A,i):  #A.size()=n+1
    if(2*i>A.size()-1):
        return
    l=2*i
    r=2*i+1
    if A[l]>A[i]:
        largest=l
    else:
        largest=i
    if A[largest]>A[r]:
        largest=r
    A[largest],A[i]=A[i],A[largest]
    max_heapify(A,largest)

def build_max_heap(A):  # A.size()=n+1
    n = A.size() - 1
    for i in range(n / 2, 0, -1):
        max_heapify(A, i)


def heapsort(A):
    build_max_heap(A)
    for i in range((A.size - 1), -1, 1):
        A[1], A[i] = A[i], A[1]
        A.size -= 1
        max_heapify(A, 1)


# priority queue
class queue:
    def __init__(self, list_A):
        self.A = list_A

    def heap_maxmum(self):
        return self.A[1]

    def max_headp_insert(self, key):
        self.A.size += 1
        self.A[self.A.size - 1] = float("-inf")
        self.heap_increase_key(self.A.size - 1, key)
    def heap_extract_max(self):
        if self.A.size < 2:
            return "heap underflow"
        max = self.A[1]
        self.A[1] = self.A[self.A.size - 1]
        self.A.size -= 1
        max_heapify(self.A, 1)

    def heap_increase_key(self, i, key):
        if key < self.A[i]:
            return "new key smaller than current key"
        self.A[i] = key
        while i > 1 and self.A[i] > self.A[i / 2]:
            self.A[i], self.A[i / 2] = self.A[i / 2], self.A[i]
            i /= 2


