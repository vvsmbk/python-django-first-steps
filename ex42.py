# Пакеты (package) в Python. Вложенные пакеты
# директория (правой кнопкой) -> package -> пакет с файлом инит
# для корректной работы все файлы в пакете должны быть в коди-
# ровке utf-8
#
import main.courses
print(dir(main.courses))  # печать того, что в ините
main.courses.html.get_html()

main.courses.get_python()
print(main.courses.python_doc.NAME)