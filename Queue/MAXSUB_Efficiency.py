import collections
def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    dq = collections.deque()
    for i in range(k):
        while(dq and arr[i]>= arr[dq[-1]]):
            dq.pop()
        dq.append(i)
    for i in range(k,n):
        print(arr[dq[0]],end=" ")
        if(dq and dq[0]<=i-k):
            dq.popleft()

        while(dq and arr[i]>=arr[dq[-1]]):
            dq.pop()
        dq.append(i)

    print(arr[dq[0]])

if __name__ == '__main__':
    main()
