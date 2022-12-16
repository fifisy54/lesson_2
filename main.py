from keras.datasets import mnist  # Библиотека с базой Mnist
from keras.models import Sequential  # Подлючаем класс создания модели Sequential
from keras.layers import Dense  # Подключаем класс Dense - полносвязный слой
from keras.optimizers import Adam  # Подключаем оптимизатор Adam
from keras import utils  # Утилиты для to_categorical
from keras.preprocessing import image  # Для отрисовки изображения
import numpy as np  # Подключаем библиотеку numpy
from mpl_toolkits.mplot3d import Axes3D  # Модуль для трехмерной графики
# from google.colab import files #Для загрузки своей картинки
import matplotlib.pyplot as plt  # Отрисовка изображений
from PIL import Image  # Отрисовка изображений

model = Sequential()
model.add(Dense(2, input_dim=2, use_bias=False))
model.add(Dense(1, use_bias=False))
print(model.summary())

weights = model.get_weights()
print(weights)

w1 = 0.42
w2 = 0.15
w3 = -0.56
w4 = 0.83
w5 = 0.93
w6 = 0.02
new_weight = [np.array([[w1, w3], [w2, w4]]), np.array([[w5], [w6]])]
print(new_weight)
model.set_weights(new_weight)

x1 = 7.2
x2 = -5.8
x_train = np.expand_dims(np.array([x1, x2]), 0)
print(x_train.shape)

# функции активации
# sigmoid
def sigmoid(x):
    return 1/(1 + np.e ** (-x))

model_sigmoid = Sequential()
model_sigmoid.add(Dense(2, input_dim=2, activation='sigmoid', use_bias=False))
model_sigmoid.add(Dense(1, activation='sigmoid', use_bias=False))
model_sigmoid.summary()
model_sigmoid.set_weights(new_weight)

y_sigmoid = model_sigmoid.predict(x_train)
print(y_sigmoid)

# relu
def relu(x):
    return np.clip(x, 0, np.inf) #от 0 до бесконечности

model_relu = Sequential()
model_relu.add(Dense(2, input_dim=2, activation='relu', use_bias=False))
model_relu.add(Dense(1, activation='relu', use_bias=False))
model_relu.summary()
model_relu.set_weights(new_weight)

y_relu = model_relu.predict(x_train)
print(y_relu)

#tanh
def th(x):
    return (np.e ** x - np.e ** (-1)) / (np.e ** x + np.e ** (-x))

model_th = Sequential()
model_th.add(Dense(2, input_dim=2, activation=th, use_bias=False))
model_th.add(Dense(1, activation=th, use_bias=False))
model_th.summary()
model_th.set_weights(new_weight)

y_th = model_th.predict(x_train)
print(y_th)


model_test = Sequential()
model_test.add(Dense(2, input_dim=2, activation='linear', use_bias=False))
model_test.add(Dense(1, activation='relu', use_bias=False))
model_test.set_weights(new_weight)

model_test.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_test.summary()

# l = model_test.train_on_batch(x_train, y_train) #вернёт ошибку
# print(l)
# print(new_weight)

# print(model_test.get_weights())
# for i in range(1000):
#   loss = model_test.train_on_batch(x_train, y_train)



#загузка базы mnist
(x_train_org, y_train_org), (x_test_org, y_test_org) = mnist.load_data()
x_train_org[0]

#картинка
n = 9
plt.imshow(x_train_org[n], cmap='viridis')
plt.show()

#нормирование и преобразование x_train и y_train
#меняем формат входных картинок
x_train = x_train_org.reshape(60000, 784)
x_test = x_test_org.reshape(10000, 784)
print(x_train_org.shape)
print(x_train.shape)
#нормализуем входные картинки
x_train = x_train.astype('float32') # x_train into float
x_train = x_train / 255 # от 0 до 1
x_test = x_test.astype('float32') # x_test into float
x_test = x_test / 255 # от 0 до 1

utils.to_categorical(y_train_org[0], 10)
y_train = utils.to_categorical(y_train_org, 10) #one_hot_encoding
y_test = utils.to_categorical(y_test_org, 10) #one_hot_encoding
print(y_train.shape)
print(y_train[n]) #один выходной вектор
print(y_train_org.shape)

#создание
model = Sequential()
model.add(Dense(800, input_dim=784, activation="relu"))
model.add(Dense(400, activation="relu"))
model.add(Dense(10, activation="softmax")) #10, тк распознаём числа от 0 до 9
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
print(model.summary())

#обучение
model.fit(x_train, y_train, batch_size=128, epochs=15, verbose=1, validation_split=0.2)

#сохраняем и загружаем веса
model.save_weights('model.h5')
model.load_weights('model.h5')

# #меняем кол-во нейронов
# model = Sequential()
# model.add(Dense(10, input_dim=784, activation="relu"))
# model.add(Dense(100, activation="linear"))
# model.add(Dense(5000, activation="softmax"))
# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# print(model.summary())
# #обучение, меняем batch_size
# model.fit(x_train, y_train, batch_size=60000, epochs=15, verbose=1, validation_split=0.2)

n_rec = 1237
plt.imshow(Image.fromarray(x_test_org[n_rec]).convert('RGBA'))
plt.show()
x = x_test[n_rec]
print(x.shape)
x = np.expand_dims(x, axis=0)
print(x.shape)
prediction = model.predict(x)
print(prediction)
prediction = np.argmax(prediction)
print(prediction)
print(y_test_org[n_rec])

my_test = Image.open('5.png').convert('L')
my_test = np.asarray(my_test).reshape(1, 784)
print(my_test)


prediction = model.predict(my_test)
print(prediction)
prediction = np.argmax(prediction)
print(prediction)


