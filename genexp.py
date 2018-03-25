import random
from time import sleep 

my_file = 'c:\\Python\\my_file'

with open(my_file, 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open(my_file)]
value_ge = (len(x) for x in open(my_file))

print("Dictionary expression presents o/p greedily (All at the same time)")
print(value)

print("Generator expression consumes iterator lazily")
while True:
    try:
        print(next(value_ge))
        sleep(1)
    except StopIteration:
        print("Iteration for generator exhausted")
        break

