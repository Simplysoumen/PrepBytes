def reverseLeftAlgo(arr,i,j):
    while(i<j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i=i+1
        j=j-1

def printArr(arr,n):
    for i in range(n):
        print(arr[i],end=' ')
    print()

def main():
    t=int(input())
    while(t>0):
        n,k=map(int,input().split())
        arr=list(map(int,input().split()))
        reverseLeftAlgo(arr,0,k-1)
        reverseLeftAlgo(arr,k,n-1)
        reverseLeftAlgo(arr,0,n-1)
        printArr(arr,n)
        t=t-1

if __name__=='__main__':
    main()
