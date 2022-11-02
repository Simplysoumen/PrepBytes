class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.addNode(self.root, data)

    def addNode(self,node,data):
        if(node is None):
            return Node(data)

        if(data < node.data):
            node.left = self.addNode(node.left, data)

        else:
            node.right = self.addNode(node.right, data)

        return node

    # def delete(self,data):
    #     self.root = self.deletionInBST(self.root, data)

    def deletionInBST(self,node,data):
        if(node is None):
            return node
        if(data < node.data):
            node.left = self.deletionInBST(node.left, data)
        elif(data > node.data):
            node.right = self.deletionInBST(node.right, data)
        else:
            if(node.left is None):
                return node.right
            elif(node.right is None):
                return node.left
            else:
                node.data = self.minValue(node.right)
                node.right = self.deletionInBST(node.right, node.data)

        return node

    def preOrderTraversal(self, node):
        if (node is None):
            return

        print(node.data, end=" ")
        self.preOrderTraversal(node.left)
        self.preOrderTraversal(node.right)

    def inOrderTraversal(self, node):
        if (node is None):
            return

        self.inOrderTraversal(node.left)
        print(node.data, end=" ")
        self.inOrderTraversal(node.right)

    def minValue(self,node):
        temp = node

        while(temp.left is not None):
            temp = temp.left

        return temp.data

def main():
    arr = list(map(int, input().split()))
    bst = BST()
    for ele in arr:
        bst.insert(ele)

    bst.preOrderTraversal(bst.root)
    print()
    bst.inOrderTraversal(bst.root)
    print()
    ele = int(input())
    bst.root = bst.deletionInBST(bst.root,ele)
    bst.inOrderTraversal(bst.root)

if __name__ == '__main__':
    main()
