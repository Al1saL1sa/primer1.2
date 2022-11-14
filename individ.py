def decator(func):

    def inner(*args, **kwargs):
        f = func(*args, **kwargs)
        print('Периметр фигуры равен {}.'.format(f))

    return inner

@decator
def basic(l):
    p = sum(l)
    return p

a = list(map(int, input("Введите длины сторон многоугольника: ").split()))
basic(a)