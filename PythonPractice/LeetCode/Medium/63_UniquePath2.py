def uniquePathsWithObstacles(obstacleGrid):
    r = len(obstacleGrid)
    c = len(obstacleGrid[0])
    if(r==0 or c==0 or obstacleGrid[r-1][c-1] == 1):
        return 0
        
    flag = False
    for j in range(1,c):
        if(obstacleGrid[0][j-1] == 1):
            flag = True
        if(flag):
            obstacleGrid[0][j] = obstacleGrid[0][j-1]

        flag = False
        
    for i in range(1,r):
        if(obstacleGrid[i-1][0] == 1):
            flag = True
        if(flag):
            obstacleGrid[i][0] = obstacleGrid[i-1][0]
        
    for i in range(r):
        for j in range(c):
            if(obstacleGrid[i][j] == 0):
                obstacleGrid[i][j] = 1
            else:
                obstacleGrid[i][j] = 0
        
    for i in range(1,r):
        for j in range(1,c):
            if(obstacleGrid[i][j] == 0):
                continue
            obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
    return obstacleGrid[r-1][c-1]

obstacleGrid = [[1,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))