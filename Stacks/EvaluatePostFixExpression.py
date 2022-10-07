class Stack:
    def __init__(self):
        self.arr = []
        self.tos = -1

    def push(self,data):
        self.tos +=1
        self.arr.append(data)

    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        self.tos = self.tos-1
        self.arr.pop()

    def size(self):
        return self.tos+1

    def isEmpty(self):
        return self.tos==-1

    def top(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        return self.arr[self.tos]
def isOp(str):
    if(str=="*"):
        return 4
    if(str=="/"):
        return 3
    if(str=="-"):
        return 2
    if(str=="+"):
        return 1
    else:
        return 0

def main():
    st = Stack()
    n = int(input())
    arr = list(input().split())
    for i in range(n):
        val = isOp(arr[i])
        if(val==0):
            st.push(int(arr[i]))
        else:
            op1 = st.top()
            st.pop()
            op2 = st.top()
            st.pop()
            if(val==4):
                st.push(op2*op1)
            if(val==3):
                st.push(op2//op1)
            if(val==2):
                st.push(op2-op1)
            if(val==1):
                st.push(op2+op1)
        print(st.top())

if __name__ == '__main__':
    main()
