
def outer_function(*msg, **punct):
    def inner_function():
        print(m for m in msg)
        print(f'Non Keyword => {msg}, Keyword args => {punct}')
    return inner_function

if __name__ == '__main__':
    print_hi = outer_function('Hi','Vipul','Howdy!',kw='first', kw2='Second',kw3='So On...')
    print_hi()
