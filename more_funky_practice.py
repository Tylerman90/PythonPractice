def integer_to_reverse_binary(integer_value):
    string = ''
    while integer_value > 0:
        rem = integer_value % 2
        string += str(rem)
        integer_value //= 2
    return string


def reverse_string(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    print(reverse_string(integer_to_reverse_binary(int(input()))))