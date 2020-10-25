def integer_to_reverse_binary(integer_value):
    binary_list = []
    while integer_value > 0:
        rem = integer_value % 2
        binary_list.append(rem)
        integer_value //= 2
    return binary_list

#def reverese_string(input_string):
    #return -1

if __name__ == '__main__':
    print(integer_to_reverse_binary(int(input())))