def countingSort(arr,n,k):
    freq = [0]*(k+1)
    for i in range(n):
        freq[arr[i]]+=1

    count = [0]*(k+1)
    count[0] = freq[0]
    for i in range(1,k):
        count[i] = count[i-1]+freq[i]

    brr = [None]*n
    for i in range(n-1,-1,-1):
        count[arr[i]]-=1
        brr[count[arr[i]]]=arr[i]

    return brr

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        max = -1
        for i in range(n):
            if(max<arr[i]):
                max = arr[i]
        k = max
        arr = countingSort(arr,n,k)
        for i in range(n):
            print(arr[i],end=' ')
        print()
        t = t-1

if __name__=='__main__':
    main()
