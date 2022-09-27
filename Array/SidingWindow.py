def main():
    t=int(input())
    while(t!=0):
        n,k = map(int, input().split())
        arr = list(map(int, input().split()))
        sum=0
        for i in range(0,k):
            sum+=arr[i]
        max=sum
        for i in range(k,n):
            sum = sum-arr[i-k]+arr[i]
            if(sum>max):
                max=sum

        print(max)
        t=t-1

if __name__=='__main__':
    main()
