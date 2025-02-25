import numpy as np

class MinMaxScalerCustom:
    def __init__(self, feature_range=(0, 1)):
        self.min = None
        self.max = None
        self.feature_range = feature_range  # Default range is (0,1)

    def fit(self, data):
        """Compute the min and max values for scaling."""
        # Minimum value for each feature
        self.min = np.min(data, axis=0)  
        # Maximum value for each feature
        self.max = np.max(data, axis=0)  

    def transform(self, data):
        """Apply the min-max scaling transformation."""
        if self.min is None or self.max is None:
            raise ValueError("Scaler has not been fitted. Call fit() before transform().")

        data_scaled = (data - self.min) / (self.max - self.min)
        return data_scaled * (self.feature_range[1] - self.feature_range[0]) + self.feature_range[0]

    def fit_transform(self, data):
        """Compute min and max, then transform the data."""
        self.fit(data)
        return self.transform(data)
