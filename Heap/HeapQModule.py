import heapq

def print_heap(heap):
    for i in range(len(heap)):
        print(heap[i], end = ' ')
    print()

def main():
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    print_heap(arr)

    heapq.heappush(arr, 100)
    print_heap(arr)

    print(heapq.heappop(arr))
    print_heap(arr)

    heapq.heapreplace(arr, 200)
    print_heap(arr)

if __name__ == '__main__':
    main()
