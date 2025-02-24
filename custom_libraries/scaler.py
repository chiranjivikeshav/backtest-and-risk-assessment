class MinMaxScalerCustom:
    def __init__(self, feature_range=(0, 1)):
        self.min = None
        self.max = None
        self.range_min, self.range_max = feature_range

    def fit(self, data):
        self.min = min(data)
        self.max = max(data)

    def transform(self, data):
        return [(x - self.min) / (self.max - self.min) * (self.range_max - self.range_min) + self.range_min for x in data]

    def inverse_transform(self, data):
        return [(x - self.range_min) / (self.range_max - self.range_min) * (self.max - self.min) + self.min for x in data]
