def fib(n,dp):
    if(n==0 or n==1):
        return n
    if(dp[n]!=-1):
        return dp[n]
    x = fib(n-1,dp)
    y = fib(n-2,dp)
    dp[n] = x+y
    return dp[n]

def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        dp = [-1 for _ in range (n+1)]
        print(fib(n,dp))
        t = t-1

if __name__ == '__main__':
    main()
