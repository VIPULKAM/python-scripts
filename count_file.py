
file_path='/tmp/pledge.txt'

def count_lines_chars(handle):
    '''
    This function returns the line count in the file.
    '''
    line_offset, char_offset, blank_space = 0, 0, 0

    for line in handle:
        for character in line:
            if character == ' ':
                blank_space += 1
                continue
            else:
                char_offset += 1
        if line:
            line_offset += 1
            continue
    return char_offset, line_offset, blank_space

with open(file_path) as f:
    char_count, line_count, blank_count = count_lines_chars(f)
    print(f"Total number of lines and characters in the file {file_path} lines: {line_count} chars:{char_count} with {blank_count} blanks")
