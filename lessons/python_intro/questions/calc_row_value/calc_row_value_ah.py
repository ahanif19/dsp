def calc_row_value(input_string):

    ''' Take an input_string. For each odd digit in the string,
        multiply the value of the digit by its position. For each
        even digit, multiply the value of digit by 5. Sum the resulting
        values and return the sum.

        Before performing the calculation, remove all white space from
        the string.

        If the input isn't a string, throw a ValueError.
    '''
    if not isinstance(input_string,str):
        raise ValueError("input_string must be a string")

    val = 0
    input_string_no_white_space = input_string.strip()
    for pos,digit in enumerate(input_string_no_white_space,1):
        if pos % 2 == 0:
            val -= int(digit)*5
        else:
            val += int(digit)*pos
    return val
