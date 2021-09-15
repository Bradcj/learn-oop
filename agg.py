def add(func):
    def dummy(*args):
        i = 0
        for num in args:
            i = num + i
        return func('Addition',i)
    return dummy

def sub(func):
    def dummy(*args):
        i = 0
        for num in args:
            i = num - i
        return func('Subtraction',i)
    return dummy

def mul(func):
    def dummy(*args):
        i = 1
        for num in args:
            i = num * i
        return func('Multiplication',i)
    return dummy

def div(func):
    def dummy(*args):
        i = 1
        for num in args:
            i = num / i
        return func('Division',i)
    return dummy
