import random
from time import sleep

with open('/tmp/my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('/tmp/my_file.txt')]
value_ge = (len(x) for x in open('/tmp/my_file.txt'))

print(value)
while True:
   try:
        print(next(value_ge))
        sleep(1)
   except StopIteration:
        print("All values in generator being consumed")
        break
