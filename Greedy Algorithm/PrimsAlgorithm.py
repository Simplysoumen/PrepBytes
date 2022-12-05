import sys
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
        if(self.adjMat[u][v]>0):
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

    def minWt(self,minimumWt, mst):
        index = -1
        for i in range(self.vertex):
            if(mst[i] is False and (index==-1 or minimumWt[index]>minimumWt[i])):
                index = i
        return index

    def primAlgo(self):
        result = [-1]*self.vertex
        mst = [False]*self.vertex
        minimumWt = [sys.maxsize]*self.vertex
        for i in range(self.vertex-1):
            minV = self.minWt(minimumWt,mst)
            mst[minV] = True
            for j in range(self.vertex):
                if(self.adjMat[minV][j]>0 and mst[j] is False):
                    if(minimumWt[j]>self.adjMat[minV][j]):
                        result[j] = minV
                        minimumWt[j] = self.adjMat[minV][j]

        for i in range(1, self.vertex):
            print("{} to {}".format(i,result[i]))

def main():
    n,e = map(int, input().split())
    graph = Graph(n)
    for i in range(e):
        u,v,w = map(int, input().split())
        graph.addEdge(u,v,w)

    graph.primAlgo()

if __name__ == '__main__':
    main()
