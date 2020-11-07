def gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a > b):
        return gcd(b, a % b)
    return gcd(a, b % a)


print('Welcome to Fraction Simplifier\nType "exit" to quit.')
while True:
    user_input = input('Enter Fraction (Int/Int):\n')
    if user_input == 'exit':
        break
    else:
        fraction = user_input.split('/')
        
        numerator = int(fraction[0])
        denominator = int(fraction[1])
        
        actual_gcd = gcd(numerator, denominator)
        
        numerator = str(int(numerator / actual_gcd))
        denominator = str(int(denominator / actual_gcd))
        
        if denominator == '1':
            print('Simplified Fraction')
            print(numerator)
        else:
            print('Simplified Fraction')
            print(numerator + '/' + denominator)
print('Bye.')
    