import sys

def mcm(arr,i,j,mini):
    if(i>=j):
        return 0
    for k in range(i,j):
        ans = mcm(arr,i,k,mini) + mcm(arr,k+1,j,mini) + (arr[i-1]*arr[k]*arr[j])
        if(mini>ans):
            mini = ans

    return mini

def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        arr = list(map(int,input().split()))
        mini = sys.maxsize
        print(mcm(arr,1,n-1,mini))
        t = t-1

if __name__ == '__main__':
     main()
