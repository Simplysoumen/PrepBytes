def main():
    t= int(input())
    while(t!=0):
        st = input()
        k,x = map(int, input().split())
        count = 0
        freq = [0]*26
        for i in range(len(st)):
            ele = ord(st[i])-97
            freq[ele]+=1
            if(freq[ele]>x):
                if(k>0):
                    freq[ele]-=1
                    k-=1
                else:
                    break
            else:
                count+=1
        print(count)
        t=t-1


if __name__=='__main__':
    main()
