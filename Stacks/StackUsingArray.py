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

def main():
    st = Stack()
    n = int(input())
    for ele in input().split():
        st.push(int(ele))
    print(st.size())
    while(st.size()!=0):
        print(st.top())
        st.pop()

if __name__ == '__main__':
    main()
