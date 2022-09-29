def sumofDigits(N):
    if(N==0 or N==1):
        return N
    else:
        return int(N%10) + sumofDigits(int(N/10))

def main():
    T = int(input())
    while(T>0):
        N = int(input())
        print(sumofDigits(N))
        T = T-1


if __name__=='__main__':
    main()
