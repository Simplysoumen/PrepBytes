def selectionSort(arr,n):
    for i in range(n):
        min_Int = i
        for j in range(i+1,n):
            if(arr[j]<arr[min_Int]):
                min_Int = j
            arr[i],arr[min_Int] = arr[min_Int],arr[i]


def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        selectionSort(arr,n)
        for i in range(n):
            print(arr[i], end=' ')
        print()
        t= t-1


if __name__ == '__main__':
    main()
