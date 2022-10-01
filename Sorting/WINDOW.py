import sys

def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        arr = list(map(int, input().split()))
        start = 0
        end = n-1
        while(start<n-1):
            if(arr[start]>arr[start+1]):
                break
            start+=1

        while(end>0):
            if(arr[end]<arr[end-1]):
                break
            end-=1

        max = -1
        min = sys.maxsize
        for i in range(start,end+1):
            if(max<arr[i]):
                max = arr[i]
            if(min>arr[i]):
                min = arr[i]

        for i in range(start):
            if(arr[i]>min):
                start = i

        for i in range(end,n):
            if(arr[i]<max):
                end = i

        print(start,end)
        t=t-1

if __name__=='__main__':
    main()
