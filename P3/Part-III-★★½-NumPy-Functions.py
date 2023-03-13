import numpy as np

def eq(A, B, p) :
    return np.mean(A == B)*100 >= p

def closest_point_indexes(points, p) :
    s = np.sqrt((points[:,0]*p[0])**2 +(points[:,1]*p[1])**2)
    n = np.arange(0,int(s.shape[0]))
    return n[s == np.min(s)]

def number_of_inversions(A) :
    x = np.ndarray(int(A.shape[0]) + 1)

exec(input().strip())