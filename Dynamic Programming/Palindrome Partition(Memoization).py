import sys

def isPalindrome(st):
    return st == st[::-1]

def palindromePartition(st,i,j,dp):
    if(i>=j):
        return 0
    if(dp[i][j]!=-1):
        return dp[i][j]
    if(isPalindrome(st[i:j+1])):
        return 0
    mini = sys.maxsize
    for k in range(i,j):
        mini = min(mini, 1 + palindromePartition(st,i,k,dp)+palindromePartition(st,k+1,j,dp))

    dp[i][j] = mini
    return dp[i][j]

def main():
    t= int(input())
    while(t!=0):
        st = input()
        n = len(st)
        dp = [[-1 for _ in range(n+1)] for _ in range (n+1)]
        print(palindromePartition(st,0,n-1,dp))
        t = t-1

if __name__ == '__main__':
    main()
