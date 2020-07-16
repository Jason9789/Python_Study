# 모듈 computing.py

def plus(x, y):
    return x + y

def minus(x, y):
    if x > y:
        return x - y
    else:
        return y - x

def multiply(x, y):
    return x * y

def divide(x, y):
    if x > y:
        if y == 0:
            return 0
        else:
            return x // y

    else:
        if x == 0:
            return 0
        else:
            return y // x
