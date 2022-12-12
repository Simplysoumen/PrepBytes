import math
import sys

def findTerm(a,b,k):
    low = 1
    high = sys.maxsize
    lcm = (a*b)//math.gcd(a,b)
    while(low<high):
        mid = (low+high)//2
        ans = mid//a + mid//b - mid//lcm
        if(ans<k):
            low = mid+1
        else:
            high = mid

    return low

def main():
    t = int(input())
    while(t!=0):
        a,b,k = map(int, input().split())
        print(findTerm(a,b,k))
        t = t-1

if __name__ == '__main__':
    main()
