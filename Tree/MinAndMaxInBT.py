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

def minValue(root):
    if (root is None):
        return 10000000000

    res = root.data
    lside = minValue(root.left)
    rside = minValue(root.right)

    if(lside<res):
        res = lside

    if(rside<res):
        res = rside

    return res

def maxValue(root):
    if (root is None):
        return -10000000000

    res = root.data
    lside = maxValue(root.left)
    rside = maxValue(root.right)

    if(lside>res):
        res = lside

    if(rside>res):
        res = rside

    return res

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
    print(minValue(root))
    print(maxValue(root))


if __name__=='__main__':
    main()
