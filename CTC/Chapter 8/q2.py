class Point:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y

#Method: 2
def is_valid(x,y,xmax,ymax,memo):
    if x>=0 and x<xmax and y<ymax and y>=0 and memo[x][y] != None:
        return True
    return False

def getPath(maze):
    if maze == None or len(maze) ==0 :
        return None
    nrow = len(maze)
    ncol = len(maze[0])
    memo = [[[]]*len(maze[0])]*len(maze)
    if maze[0][0] == 0:
        return None
    memo[0][0] = [(0,0)]
    for i in range(0,len(maze)):
        for j in range(0,len(maze[0])):
            if i==0 and j==0:
                continue
            if maze[i][j] == 0:
                memo[i][j] = None
            else:
                if is_valid(i-1,j,nrow,ncol,memo) == True:
                    p = (i,j)

                    temp = memo[i-1][j]
                    temp.append(p)
                    memo[i][j] = temp[:]
                    #print([p,memo[i][j]])
                    continue
                if is_valid(i,j-1,nrow,ncol,memo) == True:
                    p = (i, j)
                    temp = memo[i][j-1][:]
                    temp.append(p)
                    memo[i][j] = temp[:]
                    #print([p, memo[i][j]])
                    continue
                memo[i][j] = None
    return memo[nrow-1][ncol-1]


maze = [[1,1,0],[0,1,1],[0,0,1]]

print(getPath(maze))

