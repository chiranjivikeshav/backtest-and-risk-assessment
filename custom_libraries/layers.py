import numpy as np

class DenseLayer:
    def __init__(self, input_size, output_size, activation='relu'):
        self.weights = np.random.randn(input_size, output_size) * 0.01  # Initialize weights
        self.biases = np.zeros((1, output_size))  # Initialize biases
        self.activation = activation
        self.output = None
        self.input = None
        self.d_weights = None
        self.d_biases = None
        self.d_input = None

    def forward(self, input_data):
        self.input = input_data
        self.output = np.dot(input_data, self.weights) + self.biases
        if self.activation == 'relu':
            self.output = np.maximum(0, self.output)
        return self.output

    def backward(self, d_output, learning_rate):
        if self.activation == 'relu':
            d_output = d_output * (self.output > 0)  # Derivative of ReLU

        self.d_weights = np.dot(self.input.T, d_output)
        self.d_biases = np.sum(d_output, axis=0, keepdims=True)
        self.d_input = np.dot(d_output, self.weights.T)

        self.weights -= learning_rate * self.d_weights
        self.biases -= learning_rate * self.d_biases
        return self.d_input

class DropoutLayer:
    def __init__(self, rate):
        self.rate = rate
        self.mask = None
        self.output = None

    def forward(self, input_data, training=True):
        if training:
            self.mask = (np.random.rand(*input_data.shape) > self.rate) / (1 - self.rate)
            self.output = input_data * self.mask
        else:
            self.output = input_data
        return self.output

    def backward(self, d_output, learning_rate):
        return d_output * self.mask

