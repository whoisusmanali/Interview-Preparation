import numpy as np

class LinearRegression:
    def __init__(self, lr = 0.001, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, x, y):
        #Fitting the best fit line y=wx+b
        n_samples, n_features = np.shape(x)
        self.weights = np.zeros(n_features)
        self.bias = 0
        

        #using gradiant decent to update the weights or bias
        for _ in range(self.n_iters):
            y_predict = np.dot(x, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(x.T, (y_predict - y))
            db = (1/n_samples) * np.sum(y_predict - y)
            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db



    def predict(self, x):
        y_predict = np.dot(x, self.weights) + self.bias
        return y_predict
        


    