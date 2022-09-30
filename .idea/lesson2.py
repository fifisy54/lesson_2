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

#train - обучающая
#validation - проверочная
#test - тестовая

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

res = pd.DataFrame()

for choice in ['model_1', 'model_2', 'model_3']:

  if choice == 'model_1':
    ### 1 вариант сети ###
    # 3 Dense, 3 Dropout, 3 BatchNormalization
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
    ### 2 вариант сети ###
    # 3 Dense, 3 Dropout
    model = Sequential()
    model.add(Dropout(0.1, input_shape=(784,)))
    model.add(Dense(800, activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(400, activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(10, activation="softmax"))

  if choice == 'model_3':
    ### 3 вариант сети ###
    # 4 Dense, 3 Dropout, 3 BatchNormalization
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

  model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.01), metrics=["accuracy"])

  if choice == 'model_1':

    for choice_dftrain in ['60000', '50000', '10000', '500']:

      if choice_dftrain == '60000':
        print('Полная обучающая выборка: ')
        history = model.fit(x_train_new, y_train_new, batch_size=256, epochs=10, validation_data=(x_val, y_val), verbose=True)

      if choice_dftrain == '50000':
        print('Обучающая выборка из 50000 картинок: ')
        history = model.fit(x_train_new[:50000], y_train_new[:50000], batch_size=256, epochs=10, validation_data=(x_val, y_val), verbose=True)

      if choice_dftrain == '10000':
        print('Обучающая выборка из 10000 картинок: ')
        history = model.fit(x_train_new[:10000], y_train_new[:10000], batch_size=256, epochs=10, validation_data=(x_val, y_val), verbose=True)

      if choice_dftrain == '500':
        print('Обучающая выборка из 500 картинок: ')
        history = model.fit(x_train_new[:500], y_train_new[:500], batch_size=256, epochs=10, validation_data=(x_val, y_val), verbose=True)

      val_accuracy = history.history['val_accuracy']
      for i in range(len(val_accuracy)):
        print("Эпоха: ", i, " точность: ", round(100*val_accuracy[i], 1), "%", sep="")

      # plt.figure(figsize=(10,10))
      # plt.plot(history.history['accuracy'], label='Доля верных ответов на обучающем наборе')
      # plt.plot(history.history['val_accuracy'], label='Доля верных ответов на проверочном наборе')
      # plt.xlabel('Эпоха обучения')
      # plt.ylabel('Доля верных ответов')
      # plt.legend()
      # plt.show()
      #
      # plt.plot(history.history['loss'], label='Ошибка на обучающем наборе')
      # plt.plot(history.history['val_loss'], label='Ошибка на проверочном наборе')
      # plt.xlabel('Эпоха обучения')
      # plt.ylabel('Ошибка')
      # plt.legend()
      # plt.show()

      # n_rec = 34
      # plt.imshow(Image.fromarray(x_test_org[n_rec]).convert('RGBA'))
      # plt.show()
      # x = x_test[n_rec]
      # print(x.shape)
      # x = np.expand_dims(x, axis=0)
      # print(x.shape)
      # prediction = model.predict(x)
      # prediction = np.argmax(prediction)
      # print(prediction)

      scores = model.evaluate(x_test, y_test, verbose=1)
      print("Верные ответы на тестовых данных, в процентах: ", round(scores[1] * 100, 4), "%", sep="")

      if os.path.isfile(f'results.csv') is False:
        df = str(round(scores[1] * 100, 4)) + "%"
        csv = pd.DataFrame({'NN_model': [choice],
                            'training_set_size': [choice_dftrain],
                            'percent_succsessful_tests': [df]})
        print('save')
        csv.to_csv(f'results.csv', index=False)
      else:
        results_df = pd.read_csv(f'results.csv')
        df = str(round(scores[1] * 100, 4)) + "%"
        train_res = pd.DataFrame(
          {'NN_model': [choice],
           'training_set_size': [choice_dftrain],
           'percent_succsessful_tests': [df]})

        results_df = pd.concat([results_df, train_res], axis=0, ignore_index=True)
        print('save')
        results_df.to_csv(f'results.csv', index=False)

  else:
    print('Полная обучающая выборка: ')
    history = model.fit(x_train_new, y_train_new, batch_size=256, epochs=10, validation_data=(x_val, y_val), verbose=True)

    val_accuracy = history.history['val_accuracy']
    for i in range(len(val_accuracy)):
      print("Эпоха: ", i, " точность: ", round(100 * val_accuracy[i], 1), "%", sep="")

    # plt.figure(figsize=(10, 10))
    # plt.plot(history.history['accuracy'], label='Доля верных ответов на обучающем наборе')
    # plt.plot(history.history['val_accuracy'], label='Доля верных ответов на проверочном наборе')
    # plt.xlabel('Эпоха обучения')
    # plt.ylabel('Доля верных ответов')
    # plt.legend()
    # plt.show()
    #
    # plt.plot(history.history['loss'], label='Ошибка на обучающем наборе')
    # plt.plot(history.history['val_loss'], label='Ошибка на проверочном наборе')
    # plt.xlabel('Эпоха обучения')
    # plt.ylabel('Ошибка')
    # plt.legend()
    # plt.show()

    scores = model.evaluate(x_test, y_test, verbose=1)
    print("Верные ответы на тестовых данных, в процентах: ", round(scores[1] * 100, 4), '%', sep="")
    if os.path.isfile(f'results.csv') is False:
      df = str(round(scores[1] * 100, 4)) + "%"
      csv = pd.DataFrame(
        {'NN_model': [choice],
         'training_set_size': [choice_dftrain],
         'percent_succsessful_tests': [df]})
      print('save')
      csv.to_csv(f'results.csv', index=False)
    else:
      results_df = pd.read_csv(f'results.csv')
      df = str(round(scores[1] * 100, 4)) + "%"
      train_res = pd.DataFrame(
        {'NN_model': [choice],
         'training_set_size': [choice_dftrain],
         'percent_succsessful_tests': [df]})

      results_df = pd.concat([results_df, train_res], axis=0, ignore_index=True)
      print('save')
      results_df.to_csv(f'results.csv', index=False)

