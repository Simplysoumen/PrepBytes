def minPlatforms(arrival, departure,n):
    arrival.sort()
    departure.sort()
    plat = 1
    result = 1
    i = 1
    j = 0
    while(i<n and j<n):
        if(arrival[i]<=departure[j]):
            plat +=1
            i +=1
        else:
            plat -=1
            j +=1
        result = max(result, plat)
    return result

def main():
    t = int(input())
    while(t!=0):
        n  =int(input())
        arrival = list(map(int, input().split()))
        departure = list(map(int, input().split()))
        print(minPlatforms(arrival,departure,n))
        t = t-1

if __name__ == '__main__':
    main()
