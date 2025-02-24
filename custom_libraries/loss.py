import numpy as np

class MeanSquaredErrorCustom:
    def forward(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)
