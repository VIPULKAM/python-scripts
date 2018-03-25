from time import sleep

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

with open('c:\\Python\\pledge.txt', 'w') as f:
    f.write(pledge)

with open('c:\\Python\\pledge.txt') as f:
    it = index_words(f)

    while True:
        try:
            print(next(it))
            sleep(1)
        except StopIteration:
            print("All blank space inexes consumed.")
            break

