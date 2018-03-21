def index_words(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

pledge = '''India is my country.
All Indians are my brothers and sisters.
I love my country, and I am proud of its rich and varied heritage.
I shall always strive to be worthy of it.
I shall give respect to my parents,
teachers and all elders and treat everyone with courtesy.
To my country and my people,
I pledge my devotion.
In their well being and prosperity alone lies my happiness.'''

with open('/tmp/pledge.txt', 'w') as f:
    f.write(pledge)

with open('/tmp/pledge.txt') as f:
    it = index_words(f)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))

