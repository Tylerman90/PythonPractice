Alphabet = [' ', '!', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
user_word = ''
i = 0
while i < len(Alphabet):
    user_input = input("Are you thinking of the following character? '{}': (y/n)\n".format(Alphabet[i]))
    if user_input == 'y' and Alphabet[i] != '!':
        user_word += Alphabet[i]
        i = 0
    elif user_input == 'n':
        i += 1
    else:
        break

print('You typed:\n{}'.format(user_word))