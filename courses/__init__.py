# прописываем, какие пакеты буду импортированы при вызове инита
from main.courses.python import get_python
# абсолютный импорт(с полным путем)
from main.courses.java import get_java# можно так
from .php import get_php
from main.courses.html import *
from .doc import java_doc, python_doc

NAME = "package courses"