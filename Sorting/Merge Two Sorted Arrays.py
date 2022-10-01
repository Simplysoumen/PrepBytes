def mergeSortedArray(arr,brr,n,m):
    arr3 = [None]*(n+m)
    i = 0
    j = 0
    k = 0
    while(i<n and j<m):
        if(arr[i]<brr[j]):
            arr3[k] = arr[i]
            k = k+1
            i = i+1
        else:
            arr3[k] = brr[j]
            k = k+1
            j = j+1
    while(i<n):
        arr3[k]= arr[i]
        k = k+1
        i = i+1
    while(j<m):
        arr3[k] = brr[j]
        k = k+1
        j = j+1
    return arr3

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        m = int(input())
        brr = list(map(int, input().split()))
        fin = mergeSortedArray(arr,brr,n,m)
        for i in range(n+m):
            print(fin[i], end=' ')
        print()
        t= t-1


if __name__ == '__main__':
    main()
