import sys

def isPalindrome(st):
    return st == st[::-1]

def palindromePartition(st,i,j):
    if(i>=j or isPalindrome(st[i:j+1])):
        return 0
    mini = sys.maxsize
    for k in range(i,j):
        mini = min(mini, 1 + palindromePartition(st,i,k)+palindromePartition(st,k+1,j))
    return mini

def main():
    t= int(input())
    while(t!=0):
        st = input()
        print(palindromePartition(st,0,len(st)-1))
        t = t-1

if __name__ == '__main__':
    main()
