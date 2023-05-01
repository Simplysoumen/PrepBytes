def main():
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(list(map(int,input().split())))
    x,y = map(int,input().split())
    dp = [[-1 for _ in range(y+1)] for _ in range(x+1)]

    dp[0][0] = mat[0][0]
    for i in range(1,x+1):
        dp[i][0] = dp[i-1][0] + mat[i][0]

    for j in range(1,y+1):
        dp[0][j] = dp[0][j-1] + mat[0][j]

    for i in range(1,x+1):
        for j in range(1,y+1):
            dp[i][j] = mat[i][j] + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

    print(dp[x][y])

if __name__ == '__main__':
    main()
