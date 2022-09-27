def main():
    t=int(input())
    while(t!=0):
        n,k = map(int,input().split())
        arr = list(map(int, input().split()))
        sum=1
        max=-1
        for i in range(0,n-k+1):
            sum=0
            for j in range(i, i+k):
                sum+=arr[j]
            if(max<sum):
                max=sum

        print(max)
        t=t-1

if __name__=='__main__':
    main()
