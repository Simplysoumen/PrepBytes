import sys

def mcm(arr,i,j,mini,dp):
    if(i>=j):
        return 0
    if(dp[i][j] != -1):
        return dp[i][j]

    else:
        dp[i][j] = sys.maxsize
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], (mcm(arr,i,k,dp) + mcm(arr,k+i,j,dp) + (arr[i-1]*arr[k]*arr[j])))

        return dp[i][j]

def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        arr = list(map(int,input().split()))
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

        mini = sys.maxsize
        print(mcm(arr,1,n-1,mini,dp))
        t = t-1

if __name__ == '__main__':
     main()
