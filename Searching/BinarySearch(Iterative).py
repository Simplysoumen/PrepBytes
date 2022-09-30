def BinarySearch(arr,n,target):
    low = 0
    high = n-1
    while(low<=high):
        mid = low+(high-low)//2
        if(arr[mid]==target):
            return mid
        if(target>arr[mid]):
            low = mid+1
        else:
            high = mid-1
    return -1

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        target = int(input())
        res = BinarySearch(arr, n, target)
        if(res==-1):
            print("Target value is not present")
        else:
            print("Target value is present at index",res)
        t =t-1

if __name__=='__main__':
    main()
