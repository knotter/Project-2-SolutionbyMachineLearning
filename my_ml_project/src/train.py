import os
import sys

print(os.path.dirname(os.path.dirname( os.path.abspath(__file__))))
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)

import my_library.Trainer as Trainer

preprocessed_train_data_path = input()
model_dump_path_base = input()

trainer = Trainer.Trainer()
X, y = trainer.load_data(preprocessed_train_data_path)

hyperparameters_SVM = [0.01, 0.1, 1, 10, 100]
hyperparameters_RF = [1, 10, 100, 1000]
param_grid = {'C' : [0.1, 1, 10],
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
              'kernel': ['rbf']}

for h in hyperparameters_SVM:
    model_dump_path_base = model_dump_path_base + str(h) + ".pkl"
    #model_dump_path_base = model_dump_path_base + str(h) + ".pkl"
    trainer.train_SVM(h, X, y)
    #trainer.train_RF(h, X, y)
#trainer.train_Grid(param_grid, X, y)
    trainer.dump_model(model_dump_path_base)
