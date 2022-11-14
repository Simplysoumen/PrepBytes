import heapq

def main():
    t = int(input())
    while(t!=0):
        n,k = map(int, input().split())
        arr = list(map(int, input().split()))
        heapq._heapify_max(arr)
        while(k!=0):
            print(heapq._heappop_max(arr), end=' ')
            k = k-1
        print()
        t = t-1

if __name__ == '__main__':
    main()
