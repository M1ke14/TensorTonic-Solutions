import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    print(data)
    data_np = np.asarray(data,dtype=np.float64)
    m,n = data_np.shape
    result=np.zeros((3,m,n))
    element_mask= data_np>threshold
    result[0]=element_mask.astype(np.float64)
    
    row_mask= np.any(data_np>threshold,axis=1)[:,np.newaxis]
    result[1]=np.where(row_mask,data_np,0.0)
    all_mask= np.all(data_np>threshold,axis=1)[:,np.newaxis]
    result[2]=np.where(all_mask,data_np,0.0)
    return result