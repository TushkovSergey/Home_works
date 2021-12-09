import time

def decorator(old_function):
    def new_function(*args, **kwargs):
        print(f'вызвана функция c аргументами {args} ')
        print(f'вызвана функция {old_function.__name__}')
        print(f'Функция вызвана {time.ctime()}')
        result = old_function(*args)
        return result
    return new_function