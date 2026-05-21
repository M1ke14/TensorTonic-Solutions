import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    data=np.array(data,dtype=np.float64)
    return np.array([data.mean(axis=axis),data.std(axis=axis),data.min(axis=axis),data.max(axis=axis)])