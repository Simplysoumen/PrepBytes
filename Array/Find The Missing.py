def getMissingNo():
    N = int(input())
    A = list(map(int, input().split()))[:N-1]
    total = (N) * (N + 1)/ 2
    sum_of_A = sum(A)
    return total - sum_of_A

def main():
    T = int(input())
    while(T>0):
        miss = getMissingNo()
        print("%d"%miss)
        T = T-1

if __name__=='__main__':
    main()
