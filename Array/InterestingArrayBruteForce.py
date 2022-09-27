def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        mini = -1
        maxj = -1
        flag=0
        for i in range(n-1):
            for j in range(i+1,n):
                if(arr[i]+arr[j]==k):
                    flag=1
                    if(j>maxj):
                        mini = i
                        maxj = j
                    elif(maxj==j and mini>i):
                        mini = i
                        maxj = j

        if(flag==0):
            print("No Answer")

        else:
            print(mini,maxj)
        t=t-1

if __name__=='__main__':
    main()
