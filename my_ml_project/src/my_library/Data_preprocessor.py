import os
import sys
import pickle
import numpy as np
import count_statistics as counter

class DataPreprocessor:
    def __init__(self, sentence_arrays, dictionary):
        self.sentence_arrays = sentence_arrays
        self.dictionary = dictionary

    def preprocess_and_dump(self, file_path):
        X_list, y_list = [], []
        for i in range(len(self.sentence_arrays)):
            sentence = self.sentence_arrays[i][0]
            count_vector = counter.count_and_vectorize(self.dictionary, sentence)
            X_list.append(count_vector)
            if self.sentence_arrays[i][4] == "0":
                y_list.append(-1)
            else:
                y_list.append(1)

        X, y = np.array(X_list), np.array(y_list)

        with open(file_path, "wb") as f:
            pickle.dump((X, y), f)
