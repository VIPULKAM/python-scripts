from time import sleep

'''def index_words(text):
    result =  []
    if text:
        result.append(0)

    for index, word in enumerate(text):
        if word == ' ':
            result.append(index + 1)
    return result'''

def index_words(text):
    if text:
        yield 0
    for index, word in enumerate(text):
        if word == ' ':
           yield index + 1

pledge = 'India is my country.All Indians are my brothers and sisters.I love my country, and I am proud of its rich and varied heritage.I shall always strive to be worthy of it.I shall give respect to my parents, teachers and all elders and treat everyone with courtesy.To my country and my people, I pledge my devotion.In their well being and prosperity alone lies my happiness.'

result = index_words(pledge)
while True:
    try:
        print(next(result))
        sleep(1/2)
    except StopIteration:
        break
