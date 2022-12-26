def backTrack(str,i):
    if(i==len(str)):
        for ele in str:
            print(ele,end="")
        print()
        return 
    
    if(str[i].isalpha()):
        old = str[i]
        if(str[i].isupper()):
            str[i] = str[i].lower()
        else:
            str[i] = str[i].upper()
        backTrack(str,i+1)
        str[i] = old

    backTrack(str,i+1)

def main():
    str = list(input())
    backTrack(str,0)
    
if __name__ == '__main__':
    main()
