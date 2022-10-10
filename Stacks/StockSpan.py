class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tos = -1

    def isEmpty(self):
        if(self.head is None):
            return True
        return False

    def push(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            self.tos += 1
            return
        newNode.next = self.head
        self.head = newNode
        self.tos += 1

    def pop(self):
        if(self.isEmpty()):
            print("Stack is Empty")
            return

        self.head = self.head.next
        self.tos -= 1

    def size(self):
        return self.tos +1

    def top(self):
        if(self.isEmpty()):
            print("Stack is Empty")
            return
        return self.head.data


def main():
    st = Stack()
    for ele in input().split():
        st.push(int(ele))
    print(st.size())
    while(st.size()!=0):
        print(st.top())
        st.pop()

if __name__ == '__main__':
    main()
