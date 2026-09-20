def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    current = begin

    for i in range(end):
        yield current
        current = func(current)


from inspect import isgenerator

gen = some_gen(2, 4, pow)
print(isgenerator(gen))
print(list(gen))

print('OK')