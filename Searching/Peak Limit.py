def findPeakElement(arr,n,low,high):
    mid = low + (high-low)//2
    if((mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid])):
        return mid
    elif(mid>0 and arr[mid-1]>arr[mid]):
        return findPeakElement(arr,n,low,mid-1)
    else:
        return findPeakElement(arr,n,mid+1,high)

from sys import setrecursionlimit
setrecursionlimit(1000000000)
def main():
    t = int(input())
    while(t>0):
        n =int(input())
        arr = list(map(int, input().split()))
        res = findPeakElement(arr,n,0,n-1)
        print(arr[res])
        t = t-1

if __name__ == '__main__':
    main()
