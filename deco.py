
import time
from functools import wraps

def decor(funct):
    def wrapper(*args):
        print("This is decorated display now!")
        return(funct(*args))
    return wrapper

class Timeit(object):
    def __init__(self, funct):
        self.funct = funct

    def __call__(self, *args):
        print("This is decorated class example")
        return self.funct(*args)

def timeit(funct):
    @wraps(funct)
    def wrapper(*args):
        n = time.ctime()
        t1 = time.time()
        p = funct(*args)
        t2 = time.time() - t1
        print (f"Start time {n} & Time elapsed {t2}")
        print (funct.__name__)
        return p
    return wrapper

@Timeit
@timeit
def display():
    #time.sleep(2)
    print("This is simple display function")


display()
