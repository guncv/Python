import numpy as np

def mult_table(nrows, ncols) :
    row = np.arange(1,nrows+1).reshape(nrows,1)
    col = np.arange(1,ncols+1)
    return row*col

exec(input().strip())