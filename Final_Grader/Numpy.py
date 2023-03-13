import numpy as np

def f1(x) :
    a = x[:-1]
    b = x[1:]
    t = b/a
    m = t[:-1]
    n = t[1:]
    k = np.isclose(m,n)
    return np.all(k)

def f2(x) :
    a = np.ndarray(x.shape)
    return a

print(f2(np.array([[1.,  2., 3., 4. ], [5.,  6., 7., 8. ]])))