class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BuildTree:
    def __init__(self):
        self.pI = 0

    def btUsingIP(self, inOrder, preOrder, st, end):
        if(st > end):
         return None

        treeNode = Node(preOrder[self.pI])
        self.pI+=1

        inInd = self.search(inOrder,st, end, treeNode.data)
        if(st==end):
            return treeNode

        treeNode.left = self.btUsingIP(inOrder,preOrder,st, inInd-1)
        treeNode.right = self.btUsingIP(inOrder, preOrder, inInd+1, end)

        return treeNode

    def search(self,arr, st, end, val):
        for i in range(st, end+1):
            if(arr[i]==val):
                return i

    def preOrder(self,root):
        if(root is not None):
            print(root.data, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)


def main():
    inOrder = list(input().split())
    preOrder = list(input().split())
    bt = BuildTree()
    root = bt.btUsingIP(inOrder,preOrder,0,len(inOrder)-1)
    bt.preOrder(root)

if __name__ == '__main__':
    main()
