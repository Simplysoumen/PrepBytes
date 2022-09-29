def fact(N):
    if(N==1 or N==0):
        return 1
    return N*fact(N-1)

from sys import setrecursionlimit
setrecursionlimit(11000)
def main():
  T = int(input())
  while(T>0):
    N = int(input())
    print(fact(N))
    T = T-1

if __name__=='__main__':
    main()


