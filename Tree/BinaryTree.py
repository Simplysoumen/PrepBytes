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

def inOrderTraversal(root):
    if (root is None):
        return

    inOrderTraversal(root.left)
    print(root.data, end=" ")
    inOrderTraversal(root.right)

def postOrderTraversal(root):
    if (root is None):
        return

    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=" ")


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)

    preOrderTraversal(root)
    print()
    inOrderTraversal(root)
    print()
    postOrderTraversal(root)

if __name__=='__main__':
    main()

