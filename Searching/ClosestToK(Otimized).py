import math
import sys

def main():
    n = int(input())
    q = int(input())
    div = []
    size = int(math.sqrt(n))+1
    for i in range(1,size):
        if(n%i==0):
            div.append(i)
            if(i !=n//i):
                div.append(n//i)

    div.sort()
    while(q!=0):
        k = int(input())
        if(k<=div[0]):
            print(div[0])
        elif(k>=div[len(div)-1]):
            print(div[len(div)-1])
        else:
            low = 0
            high = len(div)-1
            flag=0
            mid=0
            while(low<high and flag==0):
                mid = low+ (high-low)//2
                if(div[mid]==k):
                    flag=1
                    print(div[mid])
                else:
                    if(k<div[mid]):
                        if(mid>0 and k>div[mid-1]):
                            if(abs(k-div[mid])>=abs(k-div[mid-1])):
                                flag=1
                                print(div[mid-1])
                            else:
                                flag=1
                                print(div[mid])
                        else:
                            high=mid

                    else:
                        if(mid<n-1 and k<div[mid+1]):
                            if(abs(k-div[mid])> abs(k-div[mid+1])):
                                flag=1
                                print(div[mid+1])
                            else:
                                flag=1
                                print(div[mid])
                        else:
                            low=mid+1

            if(flag==0):
                print(div[mid])

        q=q-1

if __name__=='__main__':
    main()

