# Запись данных в файл в текстовом и бинарном режимах
# при открывании на запись удаляется все содержимое в файле
# с ключом "a" файл не перезапишется, а данные дозапишутся в конец
# "a+" - разрешает и чтение, и запись в файл
import pickle

try:
    with open("out.txt", "a+") as file:
        file.seek(0)  # указать файловую позицию для чтения
        file.write("Hello4 world!\n")
        file.write("Hello1 world!\n") # строки идут друг за другом
        file.write("Hello2 world!\n")
        file.writelines(["shit\n", "beach"])
        print(file.readlines())
except:
    print("Ошибка при работе с файлом")

books = [
    ("Book1", 200),
    ("Book2", 230),
    ("Book3", 250),
    ("Book4", 100)
]

book1 = ["Book1", 200]
book2 = ["Book2", 230]
book3 = ["Book3", 250]
book4 = ["Book4", 100]

file = open("out2.bin", "wb")  # записать в бинарном режиме доступа
pickle.dump(books, file)  # записать произвольные данные в файл
file.close()

file = open("out2.bin", "rb")  # прочитать в бинарном режиме доступа
print(pickle.load(file))  # прочитать произвольные данные из файла
file.close()

try:# чтение и запись множества элементов в бинарном режиме доступа
    with open("out3.bin", "wb") as file:
        pickle.dump(book1, file)
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)
except:
    print("Ошибка при работе с файлом")

try:
    with open("out3.bin", "rb") as file:
        print(pickle.load(file))
        print(pickle.load(file))
        print(pickle.load(file))
        print(pickle.load(file))
except:
    print("Ошибка при работе с файлом")