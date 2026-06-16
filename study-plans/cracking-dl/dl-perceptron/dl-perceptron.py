import numpy as np

def perceptron(X, y, lr=0.1, epochs=100):
    """
    Returns: Tuple of (weights as list of floats, bias as float)
    """
    X=np.asarray(X,dtype=np.float64)
    y=np.asarray(y,dtype=np.float64)
    n,d=X.shape
    weights=np.zeros(d)
    b=0.0
    for _ in range(epochs):
        for i in range(n):
            z=np.dot(weights,X[i])+b
            if z>=0:
               y_pred=1
            else:
               y_pred=0
            error= y[i]-y_pred
            weights+=lr * error * X[i]
            b+=lr*error
        
    return weights.tolist(),float(b)
        