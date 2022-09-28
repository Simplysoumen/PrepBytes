def main():
    t=int(input())
    while(t!=0):
        n,q=map(int, input().split())
        st= list(input())
        freq= [0]*26
        for ele in st:
            freq[ord(ele)-97]+=1

        for i in range(q):
            m = int(input())
            count = 0
            for j in range(26):
                if(freq[j]>m):
                    count += (freq[j]-m)
            print(count)
        t=t-1


if __name__ == '__main__':
    main()
