import heapq
def print_heap(heap):
    for i in range(len(heap)):
        print(heap[i], end = ' ')
    print()

def main():
    arr =list(map(int, input().split()))

    heapq._heapify_max(arr)
    print(arr)

    print(heapq._heappop_max(arr))
    print_heap(arr)

    heapq._heapreplace_max(arr,-1)
    print_heap(arr)

    arr.append(1000)
    heapq._siftdown_max(arr, 0, len(arr)-1)
    print_heap(arr)


if __name__ == '__main__':
    main()
