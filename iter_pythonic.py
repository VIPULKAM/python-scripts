# Data in millions who visited one of US state:: Data = [22, 45, 16]
path = 'c:\\Python\\my_numbers.txt'

class Read_Visits(object):

    def __init__(self, data_path):
        self.data_path = data_path
        self.count = 0

    def __iter__(self):
        self.count += 1
        print(self.count)  # To print the number of times __iter__() called
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

def normalize(visits):
    '''
    This function calculating the % visitors based on data
    '''
    if iter(visits) is iter(visits):
        raise TypeError('Please pass container')

    result = []
    total_visits = sum(visits)

    for visit in visits:
        percent = 100 * visit / total_visits
        result.append(percent)
    return result

it = Read_Visits(path)
print(normalize(it))

'''path = '/tmp/my_numbers.txt'
data = [18, 45, 15]
with open(path, 'w') as f:
    for i in data:
        f.write(f'{i}\n')

# Functional implementation without generators

def read_visits(file_path):
    with open(file_path) as f:
        for line in f:
            yield int(line)
'''
