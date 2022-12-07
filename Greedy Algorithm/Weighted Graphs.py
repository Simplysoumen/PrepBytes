class Graph:
    def __init__(self, n):
        self.vertex = n
        self.adjMat = []
        for i in range(self.vertex):
            self.adjMat.append([0]*self.vertex)

    def addEdge(self,u,v,w):
        self.adjMat[u][v] = w
        self.adjMat[v][u] = w

    def edgePresent(self,u,v):
        if(self.adjMat[u][v]!=0):
            return True
        else:
            return False

    def removeEdge(self,u,v):
        if(self.edgePresent(u,v)):
            self.adjMat[u][v] = 0
            self.adjMat[v][u] = 0

    def printMat(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print("Weight of edge from {} to {} is {}".format(i,j,self.adjMat[i][j]),end=' ')
                print()

def main():
    n,e = map(int, input().split())
    graph = Graph(n)
    for i in range(e):
        u,v,w = map(int, input().split())
        graph.addEdge(u,v,w)

    graph.printMat()

if __name__ == '__main__':
    main()
