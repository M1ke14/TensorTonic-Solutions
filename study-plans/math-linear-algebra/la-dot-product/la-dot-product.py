import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    x=np.asarray(x,dtype=np.float32)
    y=np.asarray(y,dtype=np.float32)

    return float(np.sum(np.dot(x,y)))