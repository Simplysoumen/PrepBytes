import math
import sys

def main():
    n = int(input())
    q = int(input())
    while(q!=0):
        k = int(input())
        temp = 0
        minDiff = sys.maxsize
        ans=0
        for i in range(1,int(math.sqrt(n))+1):
            if(n%i==0):
                temp=abs(k-i)
                if(minDiff>temp):
                    minDiff=temp
                    ans=i

                if(n//i !=i):
                    temp = abs(k-n//i)
                    if(minDiff >= temp):
                        minDiff = temp
                        ans=n//i

        print(ans)
        q=q-1


if __name__ =='__main__':
    main()
