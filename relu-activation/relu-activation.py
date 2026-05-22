import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x=np.array(x,dtype=np.float64)
    x=np.where(x<0,0,x)
    return x