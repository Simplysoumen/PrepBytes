def lcs(st1,st2,n,m,dp):
    if(n==0 or m==0):
        return 0
    if(dp[n][m]!=-1):
        return dp[n][m]
    elif(st1[n-1] == st2[m-1]):
        dp[n][m] = 1 + lcs(st1, st2, n-1, m-1,dp)
    else:
        dp[n][m] = max(lcs(st1,st2,n,m-1,dp), lcs(st1,st2,n-1,m,dp))
    return dp[n][m]

def main():
    t = int(input())
    while(t!=0):
        st1 = input()
        st2 = input()
        n = len(st1)
        m = len(st2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        print(lcs(st1,st2,n,m,dp))
        t = t-1

if __name__ == '__main__':
    main()
