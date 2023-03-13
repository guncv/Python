import numpy as np

def sum_2_rows(M) :
    return M[::2,:] + M[1::2,:]

def sum_left_right(M) :
    return M[:,:int(M.shape[1])//2] + M[:,int(M.shape[1])//2:]

def sum_upper_lower(M) :
    return M[:int(M.shape[0])//2,:] + M[int(M.shape[0])//2:]

def sum_4_quadrants(M):
    Q1 = M[:int(M.shape[0])//2,:int(M.shape[1])//2]
    Q2 = M[:int(M.shape[0])//2,int(M.shape[0])//2:]
    Q3 = M[int(M.shape[0])//2:,int(M.shape[0])//2:]
    Q4 = M[int(M.shape[0])//2:,:int(M.shape[0])//2]
    return Q1 + Q2 + Q3 + Q4

def sum_4_quadrants(M) :
    return M[::2,::2] + M[1::2,::2] + M[::2,1::2] + M[1::2,1::2]

def count_leap_years(M) :
    M -= 543
    nyears = M[((M%4 == 0) & (M%100 != 0)) | \
        ((M%4 == 0) & (M%100 == 0) & (M%400 == 0))]
    return nyears.shape[0]

exec(input().strip())