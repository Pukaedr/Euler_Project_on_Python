#Euler_Project_on_Python    #by Pukaedr
n = 21
m = 21
matrix = [0] * n
for i in range(n):
    matrix[i] = [0] * m
for i in range (21):
    matrix[i][0]=1
    matrix[0][i]=1
for i in range (1,21):
    for j in range (1,21):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
for i in range (21):
    print(matrix[i])
    print("",end='')