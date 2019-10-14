import numpy as np
import pandas as pd

data = pd.read_csv('polbooks.csv')
A = data.values.tolist()
print('edges',len(A))
max=max(A)
if(max[0]>max[1]):
    size=max[0]
else:
    size=max[1]
# print('number of nodes',size)
matrix = [[0]*size for i in range(size)]
#print(matrix)
for i in range(0,len(data)): #read all of edges
    buff=A[i]                 #edge number i
    p=buff[0]            #first node
    q=buff[1]            #second node
    matrix[p-1][q-1]=matrix[q-1][p-1]=1
print(matrix)
np.savetxt("polbooks-adjMatrix.csv", matrix, delimiter=",")