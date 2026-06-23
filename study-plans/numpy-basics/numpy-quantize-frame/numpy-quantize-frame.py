import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    data=np.array(data,dtype=np.float64)
    quantize=np.stack([
        np.pad(np.round(data,decimals),pad_width,mode='constant',constant_values=0),
         np.pad(np.floor(data),pad_width,mode='constant',constant_values=0),
         np.pad(np.ceil(data),pad_width,mode='constant',constant_values=0),])
    return quantize