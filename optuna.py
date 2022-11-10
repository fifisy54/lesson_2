from keras.models import Sequential
from keras.datasets import mnist
from keras import utils #для to_categorical
from keras.preprocessing import image
from keras.optimizers import Adam
from keras.optimizers import Adadelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense, Activation, Dropout, BatchNormalization
import os
import optuna

def objective(trial):

    train_batch_size = trial.suggest_int('train_batch_size', 50, 256)
    choice = trial.suggest_categorical('model', ['model_1', 'model_2', 'model_3'])
    validational_window = trial.suggest_int('validational_window', 500, 60000)
    epochs = trial.suggest_int('epochs', 1, 30)
    learning_rate = trial.suggest_float('learning_rate', 0.001, 0.1)

    (x_train_org, y_train_org), (x_test_org, y_test_org) = mnist.load_data()

    x_train = x_train_org.reshape(60000, 784)
    x_test = x_test_org.reshape(10000, 784)

    x_train = x_train.astype('float32')
    x_train = x_train / 255
    x_test = x_test.astype('float32')
    x_test = x_test / 255

    utils.to_categorical(y_train_org[0], 10)
    y_train = utils.to_categorical(y_train_org, 10)
    y_test = utils.to_categorical(y_test_org, 10)

    x_train_new, x_val, y_train_new, y_val = train_test_split(x_train, y_train, test_size=0.2)

    if choice == 'model_1':
        model = Sequential()
        model.add(Dropout(0.1, input_shape=(784,)))
        model.add(BatchNormalization())
        model.add(Dense(800, activation="relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
        model.add(Dense(400, activation="relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
        model.add(Dense(10, activation="softmax"))

    if choice == 'model_2':
        model = Sequential()
        model.add(Dropout(0.1, input_shape=(784,)))
        model.add(Dense(800, activation="relu"))
        model.add(Dropout(0.4))
        model.add(Dense(400, activation="relu"))
        model.add(Dropout(0.4))
        model.add(Dense(10, activation="softmax"))

    if choice == 'model_3':
        model = Sequential()
        model.add(Dropout(0.1, input_shape=(784,)))
        model.add(Dense(800, activation="relu"))
        model.add(BatchNormalization())
        model.add(Dropout(0.4))
        model.add(Dense(400, activation="relu"))
        model.add(Dropout(0.5))
        model.add(BatchNormalization())
        model.add(Dense(200, activation="relu"))
        model.add(BatchNormalization())
        model.add(Dense(10, activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=learning_rate), metrics=["accuracy"])

    history = model.fit(x_train_new[:validational_window], y_train_new[:validational_window], batch_size=train_batch_size, epochs=epochs,
                        validation_data=(x_val, y_val), verbose=True)

    scores = model.evaluate(x_test, y_test, verbose=1)
    model.save_weights(f'output/{choice}_{choice_dftrain}_{train_batch_size}_{epochs}_{learning_rate}_{validational_window}_{round(scores[1] * 100, 4)}.h5')

    if os.path.isfile(f'results.csv') is False:
        df = str(round(scores[1] * 100, 4))
        csv = pd.DataFrame({'NN_model': [choice],
                            'training_set_size': [choice_dftrain],
                            'train_batch_size': [train_batch_size],
                            'validational_window' : [validational_window],
                            'epochs' : [epochs],
                            'learning_rate' : [learning_rate],
                            'percent_succsessful_tests': [df]})
        print('save')
        csv.to_csv(f'results.csv', index=False)
    else:
        results_df = pd.read_csv(f'results.csv')
        df = str(round(scores[1] * 100, 4))
        train_res = pd.DataFrame(
            {'NN_model': [choice],
             'training_set_size': [choice_dftrain],
             'train_batch_size': [train_batch_size],
             'validational_window': [validational_window],
             'epochs': [epochs],
             'learning_rate': [learning_rate],
             'percent_succsessful_tests': [df]})

        results_df = pd.concat([results_df, train_res], axis=0, ignore_index=True)
        print('save')
        results_df.to_csv(f'results.csv', index=False)
    return scores

if __name__ == "__main__":

    study = optuna.create_study(direction='maximize',
                                sampler=TPESampler())
    study.optimize(objective, n_trials=100)
    fig = optuna.visualization.plot_param_importances(study)
    plotly.offline.plot(fig, filename='Optuna_hypImportances.html')

