import numpy as np
from numpy import hstack, vstack, array

def hilbert_indices(N):
    """Return 2d hilbert indices array. Shape is (2^N, 2^N)"""
    m = array([[0]], dtype=np.int)
    for i in range(N):
        d = 4**i
        m = vstack( (hstack( (m.T, m.T[::-1, ::-1] + 3*d )),
                     hstack( (m+d, m+2*d) ) ) )
    return m
