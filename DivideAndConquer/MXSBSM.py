def maximumSum(arr,low,high):
    if(low == high):
        return arr[low]
    mid = (low+high)//2

    leftMax = float('-inf')
    sum = 0
    for i in range(mid,low-1,-1):
        sum +=arr[i]
        if(sum>leftMax):
            leftmax = sum

    rightMax = float('-inf')
    sum =0
    for i in range(mid+1,high+1):
        sum +=arr[i]
        if(sum>rightMax):
            rigthMax = sum

    maxLeftArr = maximumSum(arr,low,mid)
    maxRightArr = maximumSum(arr,mid+1,high)

    return max(maxLeftArr,maxRightArr,leftMax+rightMax)

def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        arr = list(map(int, input().split()))
        print(maximumSum(arr,0,n-1))
        t = t-1

if __name__ == '__main__':
    main()
