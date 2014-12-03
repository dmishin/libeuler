#Tools for image processing
import numpy as np
from numpy import histogram

def value_diapason(x, percent=0.95, nbins=100):
    """Use histogram to determine diapason of values, covering 95% of values in the array
    Arguemnts:
    - nbins: how many hystogram bins to use. Bigger number gives more precise results, but it is rarely needed.
    - percent: what percent of values must cover the diapason. Value between 0 and 1
    """
    if percent < 0: raise ValueError("Percent can't be negative")
    if percent > 1: raise ValueError("Percent can't be > 1")
    counts, bins = histogram(x.ravel(),nbins)
    total = sum(counts)
    accum = 0
    low = bins[-1]
    high = bins[0]
    for i, cnt in sorted( enumerate(counts), 
                          key = (lambda i_c: i_c[1]),
                          reverse=True ):
        accum += cnt
        low = min(low, bins[i])
        high = max(high, bins[i+1])
        if accum > percent * total:
            break
    return low, high

