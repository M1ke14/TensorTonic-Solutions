import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x,dtype=np.float64)
    x=1/(1+np.exp(-x))
    return x