def isValid(x,y,board,n):
    if(x>=0 and y>=0 and x<n and y<n and board[x][y]==-1):
        return True
    return False

def knightTour(board,n,move_x,move_y,curr_x,curr_y,pos):
    if(pos==n*n):
        return True

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isValid(new_x,new_y,board,n)):
            board[new_x][new_y] = pos
            if(knightTour(board,n,move_x,move_y,new_x,new_y,pos+1)):
                return True
            board[new_x][new_y] = -1
    return False

def main():
    n = int(input())
    board = [[-1 for i in range(n)] for i in range(n)]
    move_x = [2,1,-1,-2,-2,-1,1,2]
    move_y = [1,2,2,1,-1,-2,-2,-1]
    board[0][0] = 0
    pos = 1
    if(not knightTour(board,n,move_x,move_y,0,0,pos)):
        print("Spolution doesn't exist")
    else:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()

if __name__ == '__main__':
    main()
