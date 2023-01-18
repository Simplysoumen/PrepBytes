def isValid(x,y,maze,N):
    if(x>=0 and y>=0 and x<N and y<N and maze[x][y]==1):
        return True
    return False

def ratMaze(maze,result,x,y,N):
    if(x == N-1 and y == N-1 and maze[x][y]==1):
        result[x][y] =1
        return True

    if(isValid(x,y,maze,N)):
        result[x][y]=1
        if(ratMaze(maze,result,x,y+1,N) == True):
            return True
        if(ratMaze(maze,result,x+1,y,N)==True):
            return True
        result[x][y]=0
        return False

def main():
    N = 4
    maze = [[1,1,0,0],
            [1,1,1,0],
            [0,0,1,0],
            [1,1,1,1]]
    result = [[0 for _ in range(4)] for _ in range(4)]
    if(ratMaze(maze,result,0,0,N) is False):
        print("Solution does not exist")
    else:
        for i in range(4):
            for j in range(4):
                print(result[i][j],end=" ")
            print()

if __name__ == '__main__':
    main()
