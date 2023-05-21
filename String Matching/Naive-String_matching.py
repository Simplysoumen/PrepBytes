def charMatch(text,pattern,i,m):
    for j in range(m):
        if(pattern[j]!=text[i+j]):
            return False

    return True

def Naive_String_Matching(text,pattern):
    n = len(text)
    m = len(pattern)
    for i in range(0,n-m+1):
        if(charMatch(text,pattern,i,m)):
            print("Pattern matches after {} shifts".format(i))
def main():
    t = int(input())
    while(t!=0):
        text = input()
        pattern = input()
        Naive_String_Matching(text,pattern)
        t = t-1

if __name__ == '__main__':
    main()
