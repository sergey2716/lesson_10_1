"""
Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.

Пример результата выполнения программы:
Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков
Вывод на консоль:
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа потоков 0:00:34.003411 # Может быть другое время
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков 0:00:20.071575 # Может быть другое время
"""

from datetime import datetime
from os import times_result
from threading import Thread
from time import sleep


def write_words(word_count,file_name):
    file = open(file_name,'a',encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i+1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10,'example1.txt')
write_words(30,'example2.txt')
write_words(200,'example3.txt')
write_words(100,'example4.txt')

time_stop = datetime.now()
times_res = time_stop - time_start
print(f'Время работы функций {times_res}')

time2_start = datetime.now()

write_words1 = Thread(target=write_words,args=(10,'example5.txt'))
write_words2 = Thread(target=write_words, args=(30,'example6.txt'))
write_words3 = Thread(target=write_words, args=(200,'example7.txt'))
write_words4 = Thread(target=write_words, args=(100,'example8.txt'))

write_words1.start()
write_words2.start()
write_words3.start()
write_words4.start()

write_words1.join()
write_words2.join()
write_words3.join()
write_words4.join()

time2_stop = datetime.now()
time2_res = time2_stop - time2_start
print(f'Время работы потоков {time2_res}')

print(f'Время работы потоков быстрее функций на {times_res- time2_res} секунд')



























