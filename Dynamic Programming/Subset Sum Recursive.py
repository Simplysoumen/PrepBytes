def subsetSum(arr,n,sum):
    if(sum==0):
        return True
    if(n==0):
        return False
    if(arr[n-1]>sum):
        return subsetSum(arr,n-1,sum)
    return subsetSum(arr,n-1,sum-arr[n-1]) or subsetSum(arr,n-1,sum)


def main():
    t = int(input())
    while(t!=0):
        n, sum = map(int, input().split())
        arr = list(map(int, input().split()))
        if(subsetSum(arr,n,sum)):
            print("YES")
        else:
            print("NO")
        t = t-1

if __name__ == '__main__':
    main()
