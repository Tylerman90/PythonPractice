#Write a program that reads a list of integers,
#and outputs whether the list contains
#all even numbers, odd numbers, or neither. 
#The input begins with an integer 
#indicating the number of integers that follow.
def user_values():
    my_list = []
    num_in_list = int(input())
    for num in range(num_in_list):
        my_list.append(int(input()))
    return my_list

def is_list_even(my_list):
    for i in my_list:
        if (i % 2 == 1):
            return False
    return True

def is_list_odd(my_list):
    for i in my_list:
        if (i % 2 == 0):
            return False
    return True


if __name__ == '__main__':
    user_list = user_values()
    if is_list_even(user_list):
        print('all even')
    elif is_list_odd(user_list):
        print('all odd')
    else:
        print('not even or odd')