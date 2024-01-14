from Decision_tree import DecisionTree
import numpy as np
from collections import Counter

class RandomForest:
    def __init__(self, n_trees=10, max_depth=10, min_samples_split=10, n_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.n_features = n_features
        self.n_trees = n_trees
        self.trees = []


    def fit(self, x, y):
        self.trees = []
        for _ in range(self.n_trees):
            tree = DecisionTree(min_samples_split= self.min_samples_split,
                        max_depth= self.max_depth,
                        n_features=self.n_features)
            x_samples, y_samples = self._bootstrap_sample(x, y)
            tree.fit(x_samples, y_samples)
            self.trees.append(tree)
            

    def _bootstrap_sample(self, x, y):
        n_sample = x.shape[0]
        idxs = np.random.choice(n_sample, n_sample, replace = True)
        return x[idxs], y[idxs]
    

    def _most_common_label(self, y):
        counter = Counter(y)
        value = counter.most_common(1)[0][0]
        return value

            

    def predict(self,x):
        prediction = np.array([tree.predict(x) for tree in self.trees])
        tree_predict = np.swapaxes(prediction, 0, 1)
        predictions = np.array([self._most_common_label(pred) for pred in tree_predict])
        return predictions