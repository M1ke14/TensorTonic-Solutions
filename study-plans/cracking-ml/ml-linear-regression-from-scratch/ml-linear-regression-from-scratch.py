import numpy as np

def linear_regression(X, y, lr, epochs):
    """
    Returns: tuple (weights, bias)
    """
    X=np.array(X,dtype=np.float64)
    row,feature=X.shape
    weight=np.zeros(feature)
    b=0.0
    print(b)
    for i in range(epochs):
        y_p=X@weight+b
        print(b)
        error=y_p-y
        der_w=(2/row)*(X.T@error)
        print(b)
        der_b=(2/row)*np.sum(error)
        weight=weight-lr*der_w
        b=b-lr*der_b
    weights = [round(float(v), 4) for v in weight]
    bias = round(float(b), 4)
    return(weights,bias)
