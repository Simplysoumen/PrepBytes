class Graph:
    def __init__(self, n):
        self.vertex = n
        self.adjMat = []
        for i in range(self.vertex):
            self.adjMat.append([0]*self.vertex)

    def addEdge(self,u,v):
        self.adjMat[u][v] = 1

    def edgePresent(self,u,v):
        if(self.adjMat[u][v]==1):
            return True
        else:
            return False

    def removeEdge(self,u,v):
        if(self.edgePresent(u,v)):
            self.adjMat[u][v] = 0
            self.adjMat[v][u] = 0

    def topologicalSorting(self,u,visited,stack):
        visited[u] = True
        for i in range(self.vertex):
            if(self.adjMat[u][i]==1 and visited[i] is False):
                self.topologicalSorting(i,visited,stack)
        stack.append(u)

    def printMat(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print(self.adjMat[i][j],end=' ')
            print()

def main():
    n,e = map(int, input().split())
    graph = Graph(n)
    for i in range(e):
        u,v = map(int, input().split())
        graph.addEdge(u,v)

    stack = []
    visited = [False]*graph.vertex
    for i in range(graph.vertex):
        if(visited[i] is False):
            graph.topologicalSorting(i, visited, stack)

    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=" ")

if __name__ == '__main__':
    main()
