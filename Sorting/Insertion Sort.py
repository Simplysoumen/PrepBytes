def insertionSort(arr,n):
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while(j>-1 and arr[j]>temp):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        insertionSort(arr,n)
        for i in range(n):
            print(arr[i], end=' ')
        print()
        t= t-1


if __name__ == '__main__':
    main()
