def knapSack(wt,profit,cap,n,dp):
    if(n==0 or cap==0):
        return 0

    if(dp[n][cap]!=-1):
        return dp[n][cap]
    if(wt[n-1]<=cap):
        x = profit[n-1] + knapSack(wt,profit,cap-wt[n-1],n-1,dp)
        y = knapSack(wt,profit,cap,n-1,dp)
        dp[n][cap] = max(x,y)
        return dp[n][cap]
    else:
        dp[n][cap] = knapSack(wt, profit, cap, n-1,dp)
        return dp[n][cap]

def main():
    t = int(input())
    for i in range(t):
        n,cap = map(int,input().split())
        wt = list(map(int,input().split()))
        profit = list(map(int,input().split()))

        dp = [[-1 for _ in range(cap+1)] for _ in range(n+1)]

        print(knapSack(wt,profit,cap,n,dp))

if __name__ == '__main__':
    main()
