# -*- coding: utf-8 -*-
"""Question no 10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ML5dtwlvcNkitHptZ2IP9C0x5ZVtxDWC
"""

matrix = [[1,2],[3,4]]
transpose=[[0,0],[0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose[j][i] = matrix[i][j]

print("the transpose of matrix is :-",transpose)