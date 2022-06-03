# Исключение FileNotFoundError и менеджер контекста
# (with) для файлов
# try:
#   блок операторов критического кода
# except:
#   блок операторов обрабатывающих исключения
# finally:
#   блок, который выполнится в любом случае
try:
    file = open("my_file.txt", encoding="UTF-8")
    try:
        s = file.readlines()
        int(s)  # строки в числа перевести не получится,
        # произойдет переход ко второму обработчику ошибок
        print(s)
    finally:  # в любом случае выполнить следующее:
        file.close()
except FileNotFoundError:  # отлавливает одно исключение
    print("Невозможно открыть файл")
except:  # отлавливает все остальные исключения
    print("Ошибка при работе с файлом")

try:
    # аналог кода в строках 10 - 17. Файл закроется автоматически
    with open("my_file.txt", encoding="UTF-8") as file:
        s = file.readlines()
        print(s)
except FileNotFoundError:  # отлавливает одно исключение
    print("Невозможно открыть файл")
except:  # отлавливает все остальные исключения
    print("Ошибка при работе с файлом")
finally:
    print(f"File closed: {file.closed}")
