class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


x = Node(10)
y = Node(20)
z = Node(30)
x.next = y
y.next = z
z.next = x
print(x)
print(y)
print(z)
print(x.next)
print(y.next)
print(z.next)

temp=x
while(True):
    print(temp.data,end=' ')
    temp=temp.next
    if(temp==x):
        break
        
