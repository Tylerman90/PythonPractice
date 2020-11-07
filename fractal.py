def fractal(length, spaces):
    if(length == 1):
        print(" "*spaces, end="")
        print("*" * length)
        return
            
    fractal(int(length / 2), spaces)
    print(" " * spaces, end="")
    print("*" * length)
    fractal(int(length / 2), int(spaces + length // 2))
        
print("Fractal Generator")

while True:
    number= input("Enter an integer > 0:\n")
    while not (number.isdigit()):
        number= input("Enter an integer > 0:\n")
    x = int(number)
    if(x > 0):
        fractal(x, 0)
        break