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
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(self, node):
    if(node is None):
        return

    print(node.data, end =" ")
    self.preOrderTraversal(node.left)
    self.preOrderTraversal(node.right)

def isCompleteBT(root):
    if(root is None):
        return True

    queue = QueueUsingList()
    queue.enqueue(root)
    flag = False
    while(queue.size>0):
        temp = queue.dequeue()
        if(temp.left is not None):
            queue.enqueue(temp.left)
        else:
            flag = True

        if(temp.right is not None):
            if(flag is True):
                return False

            queue.enqueue(temp.right)
        else:
            flag = True
    return True

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.left.right = Node(8)

    if(isCompleteBT(root)):
        print("Tree is Complete Binary Tree")
    else:
        print("Tree is not a complete Binary Tree")

if __name__ == '__main__':
    main()
