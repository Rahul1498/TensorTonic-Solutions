import numpy as np

def mean_squared_error(y_pred, y_true):
    mse=0
    for i in range(len(y_pred)):
        stp=(y_pred[i]-y_true[i])
        mse=mse+(stp*stp)
    mse=mse/len(y_pred)
    return mse

