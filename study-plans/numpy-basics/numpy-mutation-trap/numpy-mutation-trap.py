import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    data = np.asarray(data,dtype=np.float64)
    clipped = np.clip(data[row_idx],lo,hi)
    return np.stack([data[row_idx],clipped])