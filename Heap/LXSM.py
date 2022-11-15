import heapq

def main():
    t = int(input())
    while(t!=0):
        str,q = input().split()
        q = int(q)
        arr = []
        for i in range(q):
            arr.append(str[i])
        heapq.heapify(arr)
        i = q
        final = ""
        while(len(arr)!=0):
            final += heapq.heappop(arr)
            if(i<len(str)):
                arr.append(str[i])
            heapq.heapify(arr)

            i = i+1
        print(final)

        t= t-1

if __name__ == '__main__':
    main()
