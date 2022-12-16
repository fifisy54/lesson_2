from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
# from sklearn.model_selection import train_test_splite
# import numpy as np
import pandas as pd
from keras.optimizers import Adam


class Model:

    def __init__(self, tesla_stock_price):
        self.tesla_stock_price = tesla_stock_price
        self.model = Sequential()

    def preprocess(self):
        self.x_train1, self.x_test, self.y_train1, self.y_test = train_test_splite(self.x, self.y, test_size=0.1)
        self.x_train, self.x_val, self.y_train, self.y_val = train_test_splite(self.x_train1, self.y_train1, train_size=0.7)

    def fit(self):
        self.model.add(Dense(200, input_dim=60))
        self.model.add(BatchNormalization())
        self.model.add(Dense(800, activation="relu"))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.4))
        self.model.add(Dense(400, activation="relu"))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.4))
        self.model.add(Dense(10, activation="softmax"))  # sigmoid?

        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # def chart(self):
    #
    #
    # def prediction(self):


tesla_stock_price = pd.read_csv('TSLA.csv')
dataset = tesla_stock_price.values[-2]  # [1243.0, ..., 1314.3]

model = Model(dataset)
# model.preprocess()
# model.fit()
# model.chart()
# model.prediction()


# for i in range(100):
#     if i % 100:
#         y = i + 50
#         print(i, y)
# history = model.fit(x_train, y_train, batch_size = 8, epochs = 3, validation_data=(x_val, y_val), verbose=1)


