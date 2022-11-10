

print("я вызван из модуля a.py")


def load_dataset():
    print("Загружаю датасет")


def main():
    print("запускаю обучение нейросети")


#
print(__name__)

if __name__ == "__main__":
    main()


