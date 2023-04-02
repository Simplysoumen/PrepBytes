def knapSack(wt,profit,cap,n):
    if(n==0 or cap==0):
        return 0

    if(wt[n-1]<=cap):
        x = profit[n-1] + knapSack(wt,profit,cap-wt[n-1],n-1)
        y = knapSack(wt,profit,cap,n-1)
        return max(x,y)
    else:
        knapSack(wt, profit, cap, n-1)

def main():
    t = int(input())
    for i in range(t):
        n,cap = map(int,input().split())
        wt = list(map(int,input().split()))
        profit = list(map(int,input().split()))

        print(knapSack(wt,profit,cap,n))

if __name__ == '__main__':
    main()
