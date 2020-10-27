def is_list_even(my_list):
    for i in my_list:
        if (i % 2 == 0):
            return 'all even'

def is_list_odd(my_list):
    for i in my_list:
        if (i % 2 == 1):
            return 'all odd'


if __name__ == '__main__':
    my_list = []
    num_in_list = int(input())
    for num in range(num_in_list):
        my_list.append(int(input()))
    return my_list

is_list_even(my_list)
is_list_odd(my_list)