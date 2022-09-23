t = int (input())
while(t>0):
    n = int (input())
    arr = list(map(int, input().split()))
    min=10000001
    max=-1
    for i in range(n):
        if(arr[i]<min):
            min=arr[i]
        if(arr[i]>max):
            max=arr[i]
    print(min,max) #printf("%d %d"%(min,max))
    t=t-1
