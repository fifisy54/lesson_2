# import nasdaqdatalink
import pandas as pd
import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras import utils


class Model:
    def __init__(self):
        self.model = Sequential()
        self.batch_size = 128
        # self.df = nasdaqdatalink.get("FRED/GDP", start_date="2010-01-01", end_date="2021-01-01")
        self.df = pd.read_csv('TSLA.csv')
        self.data = np.asarray(self.df[['Value']]).flatten()
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None

    def preprocess(self):
        plt.plot(self.data)
        plt.show()
        x, y = list(), list()
        for i in range(len(self.data)):
            last_index = i + 5
            if last_index > len(self.data)-1:
                break
            x.append(self.data[i:last_index])
            y.append([self.data[last_index]])
        x, y = np.array(x), np.array(y)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.3)

    def fit(self):
        self.model.add(Dense(64, input_dim=5))
        self.model.add(BatchNormalization())
        self.model.add(Dense(16))
        self.model.add(BatchNormalization())
        self.model.add(Dense(1, activation='relu'))
        self.model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    def chart(self):
        history = self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=10,
                                 validation_split=0.2, verbose=1)
        plt.figure()
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(history.history['mae'])
        plt.plot(history.history['val_mae'])
        plt.title('model mae')
        plt.ylabel('mae')
        plt.xlabel('epoch')
        plt.legend()
        plt.show()

        self.model.summary()

    def prediction(self):
        n = 1
        prediction = self.model.predict(self.x_test)
        print('Вывод сети: ', prediction[n])
        print('Верный ответ: ', np.argmax(self.y_test[n]))


model = Model()
model.preprocess()
model.fit()
model.chart()
model.prediction()
