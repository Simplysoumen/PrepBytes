# def main():
#     t = int(input())
#     while(t!=0):
#         n = int(input())
#         if(n==0 or n==1):
#             print(n)
#         else:
#             i = 1
#             while(i*i<=n):
#                 i = i+1
#             print(i-1)
#         t = t-1
#
# if __name__ == '__main__':
#     main()

def squareRoot(n):
    if(n==0 or n==1):
        return n
    low = 1
    high = n//2
    ans = 1
    while(low<=high):
        mid = (low+high)//2
        if(mid*mid == n):
            return mid
        if(mid*mid < n):
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return ans

def main():
    t = int(input())
    while(t!=0):
        n = int(input())
        print(squareRoot(n))
        t = t-1

if __name__ == '__main__':
    main()
