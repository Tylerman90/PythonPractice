user_string = input('Enter a sentence or phrase:\n')
print()
print('You entered: {}'.format(user_string))
print()

def get_num_of_characters(user_string):
	charCount = 0
	for char in range(0, len(user_string)):
		charCount += 1
	return charCount

if __name__ == '__main__':

	def output_without_whitespace(user_string):
		new_string = ''
		for char in range(0, len(user_string)):
			if user_string[char] != ' ':
				new_string += user_string[char]
		return new_string

print('Number of characters: {}'.format(get_num_of_characters(user_string)))
print('String with no whitespace: {}'.format(output_without_whitespace(user_string)))