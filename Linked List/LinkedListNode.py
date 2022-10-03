class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

x = Node(10)
y = Node(20)
print(x)
print(y)
x.next = y
print(x.next)
print(y.data)
print(y.next)
print(x.data)

print(x.next.data)
