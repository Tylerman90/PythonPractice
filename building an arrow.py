base_height = int(input('Enter arrow base height:\n'))
base_width = int(input('Enter arrow base width:\n'))
head_width = int(input('Enter arrow head width:\n'))
while head_width <= base_width:
    head_width = int(input('Enter arrow head width:\n'))
    
print()

for num in range(base_height):
    print('*' * base_width)
    
i = 0
for num in range(head_width):
    print('*' * (head_width - i))
    i += 1
    