import collections

def isValid(mat,x,y,visited,N,M):
    if(x>=0 and x<N and y>=0 and y<M and mat[x][y]==1 and visited[x][y]==False):
        return True
    return False

def BFS(mat, visited, i, j, N, M):
    que = collections.deque()
    que.append((i,j))
    visited[i][j] = True
    row = [-1,-1,-1,0,1,0,1,1]
    col = [-1,1,0,-1,-1,1,0,1]
    while(que):
        x,y = que.popleft()
        for k in range(8):
            if(isValid(mat, x+row[k], y+col[k], visited, N, M)):
                visited[x+row[k]][y+col[k]] = True
                que.append((x+row[k],y+col[k]))

def main():
    mat = [
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
        [1, 0, 0, 0]
    ]
    N = 6
    M = 4
    visited = [[False for x in range(M)] for y in range(N)]
    islands = 0
    for i in range(N):
        for j in range(M):
            if(visited[i][j] == False and mat[i][j] == 1):
                BFS(mat,visited,i,j,N,M)
                islands +=1
    print("Number of islands = ", islands)

if __name__ == '__main__':
    main()
