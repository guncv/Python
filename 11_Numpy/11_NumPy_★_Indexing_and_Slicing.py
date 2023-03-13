import numpy as np

def get_column_from_bottom_to_top(A,c):
    return A[::-1,c]

def get_odd_rows(A) :
    return A[1::2,:]

def get_even_column_last_row(A):
    return A[-1,::2]

def get_diagonal1(A) :
    return np.array([A[i,i] for i in range(int(A.shape[0]))])

def get_diagonal2(A) :
    return np.array([A[i,int(A.shape[0])-i-1] for i in range(int(A.shape[0]))])

exec(input().strip())