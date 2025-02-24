import numpy as np

class LSTMCustom:
    def __init__(self, input_size, hidden_size):
        self.hidden_size = hidden_size
        self.input_size = input_size

        # Initialize weight matrices
        self.Wf = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wi = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wo = np.random.randn(hidden_size, hidden_size + input_size)
        self.Wc = np.random.randn(hidden_size, hidden_size + input_size)

        # Initialize biases
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))
        self.bc = np.zeros((hidden_size, 1))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def tanh(self, x):
        return np.tanh(x)

    def forward(self, x, h_prev, c_prev):
        concat = np.vstack((h_prev, x))  

        # Compute gate activations
        ft = self.sigmoid(np.dot(self.Wf, concat) + self.bf)
        it = self.sigmoid(np.dot(self.Wi, concat) + self.bi)
        ot = self.sigmoid(np.dot(self.Wo, concat) + self.bo)
        c_tilde = self.tanh(np.dot(self.Wc, concat) + self.bc)

        # Update cell state and hidden state
        c_next = ft * c_prev + it * c_tilde
        h_next = ot * self.tanh(c_next)

        return h_next, c_next

class DenseCustom:
    def __init__(self, input_size, output_size):
        self.W = np.random.randn(output_size, input_size)
        self.b = np.zeros((output_size, 1))

    def forward(self, x):
        return np.dot(self.W, x) + self.b

class DropoutCustom:
    def __init__(self, rate):
        self.rate = rate

    def forward(self, x):
        mask = np.random.rand(*x.shape) > self.rate  
        return x * mask / (1 - self.rate)  
