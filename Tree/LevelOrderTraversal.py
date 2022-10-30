class QueueUsingList:
    def __init__(self):
        self.que = []
        self.size = 0
        self.front = 0

    def enqueue(self,data):
        self.que.append(data)
        self.size+=1

    def isEmpty(self):
        return self.size==0

    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return

        temp = self.que[self.front]
        self.front +=1
        self.size -=1
        return temp

    def frontele(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return
        return self.que[self.front]

    def printQueue(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return

        for i in range(self.size):
            print(self.que[self.front + i],end=" ")
        print()

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(root):
    if(root is None):
        return

    print(root.data, end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def levelOrderTraversal(root):
    if (root is None):
        return

    queue = QueueUsingList()
    queue.enqueue(root)
    while(queue.size>0):
        temp= queue.dequeue()
        print(temp.data, end=" ")

        if(temp.left is not None):
            queue.enqueue(temp.left)

        if(temp.right is not None):
            queue.enqueue(temp.right)
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.left.right.left = Node(9)
    root.left.left.right.left.left = Node(10)
    levelOrderTraversal(root)


if __name__=='__main__':
    main()
