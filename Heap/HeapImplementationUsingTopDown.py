def parent(i):
    return (i-1)//2

def left(i):
    return (2*i)+1

def right(i):
    return (2*i)+2

def heapify_up(heap, i):
    while(i!=0 and heap[parent(i)]>heap[i]):
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i=parent(i)

def insert(heap, i, ele):
    heap[i] = ele
    heapify_up(heap, i)

def print_heap(heap,n):
    for i in range(n):
        print(heap[i], end=' ')
    print()

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        heap = [None]*n
        i = 0
        for ele in input().split():
            insert(heap, i, int(ele))
            i = i+1

        print_heap(heap, n)
        t = t-1

if __name__ == '__main__':
    main()
