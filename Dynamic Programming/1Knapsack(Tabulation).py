# def knapSack(wt,profit,cap,n,dp):
#     if(n==0 or cap==0):
#         return 0
#
#     if(dp[n][cap]!=-1):
#         return dp[n][cap]
#     if(wt[n-1]<=cap):
#         x = profit[n-1] + knapSack(wt,profit,cap-wt[n-1],n-1,dp)
#         y = knapSack(wt,profit,cap,n-1,dp)
#         dp[n][cap] = max(x,y)
#         return dp[n][cap]
#     else:
#         dp[n][cap] = knapSack(wt, profit, cap, n-1,dp)
#         return dp[n][cap]

def main():
    t = int(input())
    for i in range(t):
        n,cap = map(int,input().split())
        wt = list(map(int,input().split()))
        profit = list(map(int,input().split()))

        dp = [[-1 for _ in range(cap+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(cap+1):
                if(i==0 or j==0):
                    dp[i][j]=0

        for i in range(1,n+1):
            for j in range(i,cap+1):
                if(wt[i-1] <= j):
                    x = profit[i-1] + dp[i-1][j-wt[i-1]]
                    y = dp[i-1][j]
                    dp[i][j] = max(x,y)
                else:
                    dp[i][j] = dp[i-1][j]

        print(dp[n][cap])

if __name__ == '__main__':
    main()
