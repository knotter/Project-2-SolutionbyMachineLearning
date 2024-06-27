import sklearn.metrics as metrics
import pickle

class Validator:
    def __init__(self):
        self.model = None
    def load_data(self, file_path):
        with open(file_path, 'rb') as f:
            X, y = pickle.load(f)
        return X, y

    def load_model(self, file_path):
        with open(file_path, 'rb') as f:
            self.model = pickle.load(f)

    def evaluate_model(self, X, y):
        y_pred = self.model.predict(X)
        accuracy = metrics.accuracy_score(y, y_pred)
        report = metrics.classification_report(y, y_pred)

        return accuracy, report