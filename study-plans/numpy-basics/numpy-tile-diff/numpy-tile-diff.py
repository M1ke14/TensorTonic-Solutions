import numpy as np

def tile_diff(data, reps):
    """Returns: np.ndarray of shape (2, m*reps, n), stacked tiled array and padded differences"""
    data = np.array(data,dtype=np.float64)
    tile=np.tile(data,(reps,1))
    print(tile,tile.shape)
    
    diff=np.diff(tile,axis=0)
    
    row,col=diff.shape
    diffe=np.pad(diff,((0,1),(0,0)))
    print(diffe, diffe.shape)
   
   
    
    return np.stack([tile,diffe])