import time
import os

def logger_path(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    def logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args)
            with open(f'{path}/log.txt', 'a', encoding='utf8') as file:
                file.write(
                f'''\nВызвана функция {old_function.__name__}\nc аргументами {args}, результат {result}\nдата и время вызова {time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())}\n{"---"*20}''')
            return result
        return new_function
    return logger