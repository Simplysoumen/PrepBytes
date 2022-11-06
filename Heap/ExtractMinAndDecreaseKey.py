class HeapImplementation:
    def __init__(self, n):
        self.size = n

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def heapify_down(self, heap, n, i):
        l = self.left(i)
        r = self.right(i)
        s = i
        if(l<n and heap[l]<heap[s]):
            s = l
        if(r<n and heap[r]<heap[s]):
            s = r

        if(s!= i):
            heap[i], heap[s] = heap[s], heap[i]
            self.heapify_down(heap,n,s)

    def build_heap(self, heap):
        for i in range(self.size//2 - 1, -1, -1):
            self.heapify_down(heap, self.size, i)

    def extract_heap(self, heap):
        temp = heap[0]
        heap[0], heap[self.size-1] = heap[self.size-1], heap[0]
        self.size = self.size-1
        self.heapify_down(heap, self.size, 0)
        return temp

    def decrease_key(self, heap, index, val):
        heap[index] = val
        self.heapify_up(heap, index)

    def heapify_up(self, heap, i):
        while(i != 0 and heap[self.parent(i)]>heap[i]):
            heap[i], heap[[self.parent(i)]] = heap[[self.parent(i)]], heap[i]
            i = self.parent(i)

    def print_heap(self, heap):
        for i in range(self.size):
            print(heap[i], end="")
        print()

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        heap = HeapImplementation(n)
        heap.build_heap(arr)
        heap.print_heap(arr)
        print(heap.extract_heap(arr))

        k = int(input())
        heap.decrease_key(arr, k, -1)
        heap.print_heap(arr)
        t = t-1

if __name__ == '__main__':
    main()
