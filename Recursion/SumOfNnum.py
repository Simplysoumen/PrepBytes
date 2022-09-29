def SumOfN(n):
    if(n==1 or n==0):
        return n
    return n+SumOfN(n-1)

from sys import setrecursionlimit
setrecursionlimit(11000)
def main():
    n = int(input())
    print(SumOfN(n))


if __name__=='__main__':
    main()

