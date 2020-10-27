'''def integer_to_reverse_binary(integer_value):
    string = ''
    while integer_value > 0:
        rem = integer_value % 2
        string += str(rem)
        integer_value //= 2
    return string


def reverse_string(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    print(reverse_string(integer_to_reverse_binary(int(input()))))'''

#-----------------------------------

'''def swap_values(user_val1, user_val2):
    return user_val2, user_val1

if __name__ == '__main__':
    a, b = swap_values(int(input()), int(input()))
    print(a,b)'''
    
#-----------------------

def exact_change(user_total):
    
    num_dollars = user_total // 100
    change = user_total % 100
    
    num_quarters = change // 25
    change = change % 25
    
    num_dimes = change // 10
    change = change % 10
    
    num_nickels = change // 5
    change = change % 5
    
    num_pennies = change // 1
    change = change % 1
    
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies
    

if __name__ == '__main__': 
    input_val = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    
    if num_dollars == 1:
        print('{} dollar'.format(num_dollars))
    elif num_dollars > 1:
        print('{} dollars'.format(num_dollars))
        
    if num_quarters == 1:
        print('{} quarter'.format(num_quarters))
    elif num_quarters > 1:
        print('{} quarters'.format(num_quarters))
        
    if num_dimes == 1:
        print('{} dime'.format(num_dimes))
    elif num_dimes > 1:
        print('{} dimes'.format(num_dimes))
        
    if num_nickels == 1:
        print('{} nickel'.format(num_nickels))
    elif num_nickels > 1:
        print('{} nickels'.format(num_nickels))
        
    if num_pennies == 1:
        print('{} penny'.format(num_pennies))
    elif num_pennies > 1:
        print('{} pennies'.format(num_pennies))
    
    if (num_dollars == 0) and (num_quarters == 0) and (num_dimes == 0) and (num_nickels == 0) and (num_pennies == 0):
        print('no change')