import math
def Rabin_Karp_Algo(text,pattern,d,q):
    n = len(text)
    m = len(pattern)
    h = int(math.pow(d,m-1))%q
    p = 0 #hash code for pattern
    t = [0]*(n-m+1) #hash cvode for each m character of text
    for i in range(m):
        p = (d*p + (ord(pattern[i])-97))%q
        t[0] = (d*t[0] + (ord(text[i])-97))%q

    for s in range(n-m+1):
        if(p==t[s]):
            if(charMatch(text,pattern,s,m)):
                print("Pattern match after {} shift".format(s))
        if(s<n-m):
            t[s+1] = ((d*(t[s] - (ord(text[s])-97)*h)) + ord(text[s+m])-97)%q

def charMatch(text,pattern,s,m):
    for j in range(m):
        if(pattern[j]!=text[s+j]):
            return False
    return True


def main():
    t = int(input())
    while(t!=0):
        text = input()
        pattern = input()
        d = 26
        q = 100000000000
        Rabin_Karp_Algo(text,pattern,d,q)
        t = t-1

if __name__ == '__main__':
    main()
