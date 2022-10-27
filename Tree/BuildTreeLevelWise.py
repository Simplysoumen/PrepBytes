from queue import Queue

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def buildTreeLevelWise(ip):
    if(len(ip)==0 or ip[0]==-1):
        return None
    root = Node(ip[0])
    qu = Queue()
    qu.put(root)
    i = 1
    while(qu.empty() is False and i<len(ip)):
        currNode = qu.get()
        currVal = ip[i]

        if(currVal != '-1'):
            currNode.left = Node(currVal)
            qu.put(currNode.left)
        i = i+1
        if(i>=len(ip)):
            break

        currVal = ip[i]
        if(currVal != -1):
            currNode.right = Node(currVal)
            qu.put(currNode.right)
        i+=1

    return root

def inOrderTraversal(root):
    if(root is not None):
        inOrderTraversal(root.left)
        print(root.data, end=" ")
        inOrderTraversal(root.right)
def main():
    ip = list(input().split())
    root = buildTreeLevelWise(ip)
    inOrderTraversal(root)

if __name__ == '__main__':
    main()
