def get_num_of_non_WS_characters(usr_str):
    non_WS = 0
    for char in range(0, len(usr_str)):
        if usr_str[char] != ' ':
            non_WS += 1
    return non_WS

def get_num_of_words(usr_str):
    word_count = 1
    first_space = True
    for char in usr_str:
        if char.isspace() and first_space:
            word_count += 1
            first_space = False
        elif not char.isspace():
            first_space = True
    return word_count

def fix_capitalization(usr_str):
    edited_text = ''
    first_letter = True
    num_of_cap = 0
    for char in usr_str:
        if first_letter and char.islower():
            edited_text += char.upper()
            num_of_cap += 1
            first_letter = False
        else:
            first_letter = False
            edited_text += char
            if char.isspace():
                first_letter = True
    return (edited_text, num_of_cap)

def replace_punctuation(usr_str, exclamation_count, semicolon_count):
    ex_count = 0
    semi_count = 0
    edited_text = ''
    for char in usr_str:
        if (ex_count <= exclamation_count) and char == '!':
            edited_text += '.'
            ex_count += 1
        elif (semi_count <= semicolon_count) and char == ';':
            edited_text += ','
            semi_count += 1
        else:
            edited_text += char
    return (edited_text, semi_count, ex_count)

def shorten_space(usr_str):
    edited_text = ''
    extra_space = False
    for char in usr_str:
        if extra_space and char.isspace():
            pass
        else:
            extra_space = False
            edited_text += char
            if char.isspace():
                extra_space = True
    return edited_text


if __name__ == '__main__':
    
    def print_menu(usr_str):
        menu_op = ''
        while menu_op != 'q':
            print('MENU')
            print('c - Number of non-whitespace characters')
            print('w - Number of words')
            print('f - Fix capitalization')
            print('r - Replace punctuation')
            print('s - Shorten spaces')
            print('q - Quit')
            print()
            menu_op = input('Choose an option:\n')
            if menu_op == 'c':
                print('Number of non-whitespace characters: {}\n'.format(get_num_of_non_WS_characters(usr_str)))
            elif menu_op == 'w':
                print('Number of words: {}\n'.format(get_num_of_words(usr_str)))
            elif menu_op == 'f':
                print('Number of letters capitalized: {}'.format(fix_capitalization(usr_str)[1]))
                print('Edited text: {}'.format(fix_capitalization(usr_str)[0]))
            elif menu_op == 'r':
                print('Punctuation replaced')
                ex = int(input('exclamation count:'))
                semi = int(input('semicolon count:'))
                print('Edited text: {}'.format(replace_punctuation(usr_str, exclamation_count = ex, semicolon_count = semi)[0]))
            elif menu_op == 's':
                print('Edited text: {}\n'.format(shorten_space(usr_str)))
            
    user_str = str(input('Enter a sample text:\n'))
    print()
    print('You entered: {}'.format(user_str))
    print()
    print_menu(user_str)