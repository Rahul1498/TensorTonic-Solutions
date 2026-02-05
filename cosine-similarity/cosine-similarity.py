import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    numerator = np.dot(a, b)
    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0  # or raise an exception if required

    return numerator / denominator
