import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))


class LogisticRegression:
    def __init__(self, lr = 0.001, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, x, y):
        n_samples, n_features = x.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            linear_predict = np.dot(x, self.weights) + self.bias
            prediction = sigmoid(linear_predict)

            dw = (1/n_samples) * np.dot(x.T, (prediction - y))
            db = (1/n_samples) * np.sum(prediction - y)

            self.weights = self.weights - self.lr*dw
            self.bias = self.bias - self.lr*db
 
    def predict(self, x):
        linear_predict = np.dot(x, self.weights) + self.bias
        prediction = sigmoid(linear_predict)

        class_predict = [0 if y<=0.5 else 1 for y in prediction]
        return class_predict