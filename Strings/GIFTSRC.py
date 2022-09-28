def main():
    t=int(input())
    while(t!=0):
        n = int(input())
        st = input()
        x=0
        y=0
        cc=''
        if(st[0]=='L'):
            x-=1
            cc='L'
        elif(st[0]=='R'):
            x+=1
            cc='R'
        elif(st[0]=='U'):
            y+=1
            cc='U'
        else:
            y-=1
            cc='D'

        for i in range(1,n):
            if(cc=='L' or cc=='R'):
                if(st[i]=='U'):
                    y+=1
                    cc='U'

                elif(st[i]=='D'):
                    y-=1
                    cc='D'
            else:
                if(st[i]=='L'):
                    x-=1
                    cc='L'
                elif(st[i]=='R'):
                    x+=1
                    cc='R'
        print(x,y)

        t=t-1

if __name__=='__main__':
    main()
