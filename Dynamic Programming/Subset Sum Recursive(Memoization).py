def subsetSum(arr,n,sum,dp):
    if(sum==0):
        return True
    if(n==0):
        return False
    if(dp[n][sum]!=None):
        return dp[n][sum]

    if(arr[n-1]>sum):
        dp[n][sum] = subsetSum(arr,n-1,sum,dp)
    else:
        dp[n][sum] = subsetSum(arr,n-1,sum-arr[n-1],dp) or subsetSum(arr,n-1,sum,dp)

    return dp[n][sum]

def main():
    t = int(input())
    while(t!=0):
        n, sum = map(int, input().split())
        arr = list(map(int, input().split()))
        dp = [[None for i in range(sum+1)] for j in range(n+1)]

        if(subsetSum(arr,n,sum,dp)):
            print("YES")
        else:
            print("NO")
        t = t-1

if __name__ == '__main__':
    main()
