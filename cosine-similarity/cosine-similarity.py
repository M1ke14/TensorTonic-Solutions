import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a=np.asarray(a,dtype=np.float32)
    b=np.asarray(b,dtype=np.float32)
    if np.linalg.norm(a)==0 or np.linalg.norm(b)==0:
        return 0.0
    res=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return float(res)
    