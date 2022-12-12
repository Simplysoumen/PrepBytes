def findClosest(arr,n,k):
    low = 0
    high = n-1
    if(k<=arr[0]):
        return arr[0]
    if(k>=arr[n-1]):
        return arr[n-1]
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]==k):
            return arr[mid]
        if(arr[mid]>k):
            if(mid!=0 and arr[mid-1]<k):
                if(arr[mid]-k<k-arr[mid-1]):
                    return arr[mid]
                else:
                    return arr[mid-1]
            else:
                high = mid-1
        else:
            if(mid < n-1 and arr[mid+1]>k):
                if(arr[mid] < arr[mid+1]-k):
                    return arr[mid]
                else:
                    return arr[mid+1]
            else:
                low = mid+1

def main():
    t = int(input())
    while(t!=0):
        n,k = map(int,input().split())
        arr = list(map(int, input().split()))
        print(findClosest(arr,n,k))
        t = t-1

if __name__ == '__main__':
    main()
