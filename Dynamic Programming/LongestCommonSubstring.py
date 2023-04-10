def main():
    t = int(input())
    while(t!=0):
        st1 = input()
        st2 = input()
        n = len(st1)
        m = len(st2)
        dp = [[-1 for _ in range (m+1)] for _ in range (n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        result = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(st1[i-1] == st2[j-1]):
                    dp[i][j] = 1+dp[i-1][j-1]
                    result = max(result,dp[i][j])
                else:
                    dp[i][j] = 0
        print(result)

        t = t-1

if __name__ == '__main__':
    main()
