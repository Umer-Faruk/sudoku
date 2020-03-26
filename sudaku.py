import numpy as np 

mat =[[1,5,4,3,6,9,8,7,2],
      [1,5,4,3,6,9,8,7,2],
      [1,5,4,3,6,9,8,7,2],
      [1,5,4,3,6,9,8,7,2],
      [1,5,4,3,6,9,8,7,2],
      [1,5,4,3,6,9,8,7,2],
      [1,5,4,3,6,9,8,7,2],
      [1,5,4,3,6,9,8,7,2],
      [1,5,4,3,6,9,8,0,2],


]

for i in range(0,9):
     for j in range(0,9):
          mat[i][j]=0

def pos(x,y,n):
     global mat
     for i in range(0,9):
         if mat[x][i] == n:
              return False
     for j in range(0,9):
          if mat[j][y] == n:
               return False
     for i in range(0,3):
          for j in range(0,3):
               if mat[i+(x//3)*3][j+(y//3)*3]==n:
                    return False
     return True

def solve():
     global mat
     print(np.matrix(mat))
     for x in range(9):
          for y in range(9):
               if mat[x][y]==0:
                    for n in range(1,10):
                         if pos(x,y,n):
                              mat[x][y]=n
                              solve()
                              mat[x][y]=0
                    return
     print(np.matrix(mat))
     input("neaxt pos")

print(np.matrix(mat))                   
solve()
print(np.matrix(mat))

               