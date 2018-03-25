file_path='c:\\Python\\pledge.txt'

class Cnt(object):
    def __init__(self, path):
        self.data_path = path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield line

def count_lines(handle):
    '''
        This function returns the line count in the file.
    '''
    offset = 0
    for line in handle:
        if line:
            offset += 1
            continue
    return offset

def count_occurnace(handle, word):
    '''
    This function returns the word pattern count in a given file
    '''
    count = 0
    for line in handle:
        if word in line:
            count += 1
    return word, count
    
ct_it = Cnt(file_path)
print(f"Total number of lines in file '{file_path}' := {count_lines(ct_it)}")

word_count = count_occurnace(ct_it, 'I')
count, word = word_count
print(f"For word \"{count}\" number of occurances are '{word}'")