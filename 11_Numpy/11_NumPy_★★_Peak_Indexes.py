import numpy as np

def peak_indexes(x) :
    m = np.arange(0,x.shape[0])
    m[1:] = x[:-1]
    m[0] = 9999
    n = np.arange(0,x.shape[0])
    n[:-1] = x[1:] 
    n[-1] = 9999
    index = np.arange(0,x.shape[0])
    return index[(x > n) & (x > m)]

def main() :
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")



exec(input().strip())
