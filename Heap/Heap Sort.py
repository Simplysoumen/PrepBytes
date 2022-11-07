def parent(i):
    return (i-1)//2

def left(i):
    return (2*i)+1

def right(i):
    return (2*i)+2

def heapify_down(heap, n, i):
    s = i
    l = left(i)
    r = right(i)
    if (l<n and heap[l]<heap[s]):
        s=l
    if(r<n and heap[r]<heap[s]):
        s=r

    if(s != i):
        heap[i], heap[s] = heap[s], heap[i]
        heapify_down(heap, n, s)

def build_heap(heap, n):
    for i in range(n//2-1, -1, -1):
        heapify_down(heap, n, i)

def heap_sort(heap, n):
    build_heap(heap,n)
    for i in range(n-1,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify_down(heap, i, 0)

def print_heap(heap,n):
    for i in range(n-1,-1,-1):
        print(heap[i], end=' ')
    print()

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        heap_sort(arr, n)
        print_heap(arr, n)
        t = t-1

if __name__ == '__main__':
    main()
