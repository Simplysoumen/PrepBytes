import sys


def main():
    t=int(input())
    while(t!=0):
        n = int(input())
        st = input()
        min = sys.maxsize
        lastOccur = [-1]*26
        for i in range(n):
            ele = ord(st[i])-97
            if(lastOccur[ele]==-1):
                lastOccur[ele]=i

            else:
                val = i - lastOccur[ele]-1
                lastOccur[ele]=i
                if(min>val):
                    min=val

        if(min==sys.maxsize):
            print(0)
        else:
            print(n-1-min)

        t=t-1

if __name__=='__main__':
    main()
