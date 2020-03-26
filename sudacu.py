import numpy as np

grid = [[1,2,3,5,4,6,8,7,9],
       [1,4,1,1,4,6,9,7,9],
       [1,4,1,1,4,6,9,7,9],
       [1,4,1,1,4,6,9,7,9],
       [1,4,1,1,4,6,9,7,9],
       [1,4,1,1,4,6,9,7,9],
       [1,4,1,1,4,6,9,7,9],
       [1,4,1,1,4,6,9,7,9],
       [1,4,1,1,4,6,9,7,9],  ]

# print(np.matrix(mat))

for i in range(1,9):
     for j in range(0,9):
          grid[i][j]=0

# print(np.matrix(mat))

# px=6
# py=1

# for i in range(0,3):
#      for j in range(0,3):
#           mat[i+(px//3)*3][j+(py//3)*3]=3

# print(np.matrix(mat))

def pos(x,y,n) :
    global grid
    for i in range(0,9):
        if grid[x][i]==n:
            return False
    for i in range(0,9):
        if grid[i][y]==n:
            return False
    for i in range(0,3):
        for j in range(0,3):
            if grid[i+((x//3)*3)][j+((y//3)*3)]==n:
                return False
    return True

def solve():
    global grid
    print(np.matrix(grid))
    for x in range(9):
        for y in range(9):
            if grid[x][y]==0:
                for n in range(1,10):
                    if pos(x,y,n):
                        grid[x][y]=n
                        solve()
                    grid[x][y]=0
                return
    print(np.matrix(grid))
    input("?")
    
solve()