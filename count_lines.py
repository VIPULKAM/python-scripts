
file_path='/tmp/pledge.txt'

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

with open(file_path) as f:
    line_count = count_lines(f)
    print("Total number of lines in {line_count}")
