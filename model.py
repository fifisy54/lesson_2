from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization
from keras import utils
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random


class Model:

    def __init__(self):
        self.model = Sequential()
        self.batch_size = 128
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()

    def preprocess(self):
        # fig, axs = plt.subplots(1, 10, figsize=(25, 3))
        # for i in range(10):
        #   label_indexes = np.where(self.y_train == i)[0]
        #   index = random.choice(label_indexes)
        #   img = self.x_train[index]
        #   axs[i].imshow(Image.fromarray(img), cmap='gray')
        # plt.show()

        self.y_train = utils.to_categorical(self.y_train, 10)
        self.y_test = utils.to_categorical(self.y_test, 10)
        self.x_train = self.x_train.reshape(self.x_train.shape[0], 28, 28, 1)
        self.x_test = self.x_test.reshape(self.x_test.shape[0], 28, 28, 1)

    def fit(self):
        self.model.add(BatchNormalization(input_shape=(28, 28, 1)))
        self.model.add(Conv2D(2, (3, 3), padding='same', activation='relu'))
        self.model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))
        self.model.add(Flatten())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(0.25))
        self.model.add(Dense(10, activation='softmax'))
        self.model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    def chart(self):
        history = self.model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=1,
                                 validation_data=(self.x_test, self.y_test), verbose=1)
        # plt.plot(history.history['accuracy'], label='Доля верных ответов на обучающей выборке')
        # plt.plot(history.history['val_accuracy'], label='Доля верных ответов на проверочной выборке')
        # plt.xlabel('Эпоха обучения')
        # plt.ylabel('Доля верных ответов')
        # plt.legend()
        # plt.show()

        self.model.summary()

    def prediction(self):
        n = 2020
        prediction = self.model.predict(self.x_test)

        print('Вывод сети: ', prediction[n])
        print('Распознанная цифра: ', np.argmax(prediction[n]))
        # print('Верный ответ: ', np.argmax(self.y_test[n]))
        return int(np.argmax(prediction[n]))




model = Model()
model.preprocess()
model.fit()
model.chart()
model.prediction()


"""
join (список из строк --> в строку с любым разделителем)
split (строку --> в список из строк по пробелу)
list comprehension (генератор списков. for if else в одну строчку в [])
dict comprehension
startswith (возвращает True False. сопоставляет начало строки с данной строкой)
upper, lower (перевод в верхний/нижний регистр)
"""

"""
Exceptions - исключения:
(try) попробуй выполнить, (except) если определенная ошибка, выведи "..."
(else) - если исключение не использовалось
(finally) - в конце. не важно, было исключение или нет
"""

"""
генераторы:
итераторы, которые создаются от функции с yield
экономят память и время
не хранит значения в памяти: выводит одно -> next() -> выводит следущее
"""

"""
итераторы:
итерируемые объекты: str, list, set, dict (т.е. все объекты, по которым можно пройтись циклом)
штука из функции iter()
работает с next()
когда элементы заканчиваются, выдает 'StopIteration'
"""

"""
память в python:
аллокатор. основная задача - оптимизация количества системных вызовов на выделение памяти
"""

