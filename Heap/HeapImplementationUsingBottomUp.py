def parent(i):
    return (i-1)//2

def left(i):
    return (2*i)+1

def right(i):
    return (2*i)+2

def build_heap(heap, n):
    for i in range(n//2-1, -1, -1):
        heapify_down(heap, n, i)

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

def print_heap(heap,n):
    for i in range(n):
        print(heap[i], end=' ')
    print()

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        build_heap(arr, n)
        print_heap(arr, n)
        t = t-1

if __name__ == '__main__':
    main()
