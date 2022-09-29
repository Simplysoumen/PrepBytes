def PrintNum(n):
    if(n==0):
        return
    print(n)
    PrintNum(n-1)

from sys import setrecursionlimit
setrecursionlimit(11000)
def main():
    n = int(input())
    PrintNum(n)


if __name__=='__main__':
    main()
