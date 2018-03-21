def check_input(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return float(x), float(y)
    else:
        return x,y

def add(x, y):
    x,y = check_input(x, y)
    return x+y

def sub(x, y):
    x,y = check_input(x, y)
    return x-y

def mul(x, y):

    x,y = check_input(x, y)
    return x*y

def div(x, y):

    x,y = check_input(x, y)
    try:
        return x/y
    except ZeroDivisionError:
        return None
