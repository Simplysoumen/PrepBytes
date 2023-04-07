def lcs(st1,st2,n,m):
    if(n==0 or m==0):
        return 0
    if(st1[n-1] == st2[m-1]):
        return 1 + lcs(st1, st2, n-1, m-1)
    else:
        return max(lcs(st1,st2,n,m-1), lcs(st1,st2,n-1,m))

def main():
    t = int(input())
    while(t!=0):
        st1 = input()
        st2 = input()
        print(lcs(st1,st2,len(st1),len(st2)))
        t = t-1

if __name__ == '__main__':
    main()
