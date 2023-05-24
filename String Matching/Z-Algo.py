def createZarr(st,z):
    n = len(st)
    l = 0
    r = 0
    for i in range(1,n):
        if(i>r):
            l = i
            r = i
            while(r<n and st[r-l]==st[r]):
                r +=1
            z[i] = r-l
            r -= 1
        else:
            k = i-l
            if(z[k]<(r-i+1)):
                z[i] = z[k]
            else:
                l = i
                while(r<n and st[r-l]==st[r]):
                    r +=1
                z[i] = r-l
                r -=1

def z_algo(text,pattern):
    st = pattern + "S" + text
    l = len(st)
    z = [0]*l
    createZarr(st,z)
    n = len(pattern)
    for i in range(l):
        if(z[i]==n):
            print("Pattern found at index=",i-n-1)

def main():
    t = int(input())
    while(t!=0):
        text = input()
        pattern = input()
        z_algo(text,pattern)
        t = t-1

if __name__ == '__main__':
    main()
