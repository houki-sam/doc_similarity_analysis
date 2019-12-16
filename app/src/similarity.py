import numpy as np

def Cos_similarity(a, b):
    # numpy.arrayに変換
    A = np.array(a)
    B = np.array(b)

    bunbo = np.dot(
        np.linalg.norm(A,axis=1,ord=2)[:,None],
        np.linalg.norm(B,axis=1,ord=2)[None,:],
        )
    bunshi = np.dot(A, B.T)
    return bunshi/bunbo
