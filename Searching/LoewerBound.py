def LowerBound(arr,n,ele):
    low = 0
    high = n
    while(low<high):
        mid = low +(high-low)//2
        if(ele<=arr[mid]):
            high = mid
        else:
            low = mid+1
    return low

from sys import setrecursionlimit
setrecursionlimit(100000000)
def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        q = int(input())
        while(q>0):
            ele = int(input())
            print(LowerBound(arr,n,ele))
            q = q-1
        t =t-1

if __name__=='__main__':
    main()
