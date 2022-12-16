try:
    with open("smth.csv", "+r") as reader:
        lines = reader.readlines()
except FileNotFoundError:
    print('файла нет')
finally:
    print('smth')
