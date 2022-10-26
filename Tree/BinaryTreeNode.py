class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def main():
    b1 = Node(1)
    b2 = Node(2)
    b3 = Node(3)
    b1.left = b2
    b1.right = b3
    print(b1,b1.left,b1.right)
    print(b2)
    print(b3)

if __name__ == '__main__':
    main()
