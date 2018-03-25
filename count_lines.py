
file_path='c:\\Python\\pledge.txt'

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
    This function returns the word count in a given file
    '''
    count = 0
    for line in handle:
        if word in line:
            count += 1
    return word, count

with open(file_path) as f:
    line_count = count_lines(f)
    print(f"Total number of lines in '{file_path}':={line_count}")

with open(file_path) as f:
    word_count = count_occurnace(f, "is")
    count, word = word_count
print(f"For word \"{count}\" number of occurances are '{word}'")