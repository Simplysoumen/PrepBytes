class Node:
    def __init__(self,v,weight):
        self.data = v
        self.wt = weight
        self.next = None

class Graph:
    def __init__(self,n):
        self.vertex = n
        self.graph = [None]*self.vertex

    def addEdge(self,u,v,w):
        newNode = Node(v,w)
        newNode.next = self.graph[u]
        self.graph[u] = newNode

        newNode = Node(u)
        newNode.next = self.graph[v]
        self.graph[v] = newNode

    def edgePresent(self,u,v):
        temp = self.graph[u]
        while(temp is not None):
            if(temp.data == v):
                return True
            temp = temp.next
        return False

    def edgeRemove(self,u,v):
        if(self.edgePresent(u,v)):
            temp = self.graph[u]


    def printGraph(self):
        for i in range(self.vertex):

            temp = self.graph[i]
            while temp:
                print("Weight of edge from {} to {} = {} ".format(i,temp.data,temp.wt))
                temp = temp.next
            print()

def main():
    n,e = map(int, input().split())
    gr = Graph(n)
    for i in range(e):
        u, v, w = map(int, input().split())
        gr.addEdge(u,v, w)

    gr.printGraph()

if __name__ == '__main__':
    main()

