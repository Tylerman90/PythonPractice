def print_pattern():
    print('*****')

print_pattern()
print_pattern()

#--------------------

def print_shape():
    print('***\n' + '***\n' + '***')
    
print_shape()

#--------------------

def output_minutes_as_hours(orig_minutes):
    print(minutes / 60) 

minutes = float(input())
output_minutes_as_hours(minutes)

#--------------------

def print_total_inches(num_feet, num_inches):
    print((num_feet * 12) + num_inches)

feet = int(input())
inches = int(input())
print_total_inches(feet, inches)
