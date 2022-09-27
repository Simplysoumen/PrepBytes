def rightRotate(arr,n):
    temp=arr[n-1]
    for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
    arr[0]=temp

def printArr(arr,n):
    for i in range(n):
        print(arr[i],end=' ')
    print()
def main():
    t=int(input())
    while(t>0):
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        for i in range(k):
                rightRotate(arr,n)
                printArr(arr,n)
                t=t-1

if __name__=='__main__':
    main()
