def fibo(N):
    if(N==1 or N==0):
        return N
    x = fibo(N-1)
    y = fibo(N-2)
    return x+y

def main():
    T = int(input())
    while(T>0):
        N = int(input())
        print(fibo(N))
        T = T-1

if __name__=='__main__':
    main()
