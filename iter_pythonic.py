# Data in millions who visited one of US state
path = '/tmp/my_numbers.txt'

class Read_Visits(object):

    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
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

''' To pass aribitary data to function '''

'''path = '/tmp/my_numbers.txt'

with open(path, 'w') as f:
    for i in data:
        f.write(f'{i}\n')
'''

def read_visits(file_path):
    '''
    This function generating the values
    '''
    with open(file_path) as f:
        for line in f:
            yield int(line)

it = Read_Visits(path)
print(normalize(it))
