def rearrange(arr,N):
    max_ele = arr[N-1]
    min_ele = arr[0]

    for i in range(N):
        if(i%2==0):
            arr[i] = max_ele
            max_ele -= 1
        else:
            arr[i] = min_ele
            min_ele += 1
def main():
    T = int(input())
    while(T>0):
        N = int(input())
        arr = list(map(int, input().split()))
        rearrange(arr,N)
        for i in range(N):
            print(arr[i],end=" ")
        print()
        T = T-1


if __name__=='__main__':
    main()


