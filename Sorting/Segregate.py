def merge(arr,temp,low,mid,high):
    k = low
    for i in range(low,mid+1):
        if(arr[i]<0):
            temp[k]=arr[i]
            k = k+1

    for j in range(mid+1,high+1):
        if(arr[j]<0):
            temp[k]=arr[j]
            k+=1
    for i in range(low,mid+1):
        if(arr[i]>=0):
            temp[k]=arr[i]
            k = k+1
    for j in range(mid+1,high+1):
        if(arr[j]>=0):
            temp[k]=arr[j]
            k += 1

    for i in range(low,high+1):
        arr[i] = temp[i]


def segregate(arr,temp,low,high):
    if(high==low):
        return
    mid = low + (high-low)//2
    segregate(arr,temp,low,mid)
    segregate(arr,temp,mid+1,high)
    merge(arr,temp,low,mid,high)


def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        arr = list(map(int, input().split()))
        temp = arr.copy()
        segregate(arr,temp,0,n-1)
        for ele in arr:
            print(ele,end=' ')
        print()
        t=t-1


if __name__ == '__main__':
    main()
