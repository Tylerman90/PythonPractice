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
    print('Total inches:', end='')
    print((num_feet * 12) + num_inches)

feet = int(input())
inches = int(input())
print_total_inches(feet, inches)

#--------------------

def c_to_f(temp_c):
    temp_f = (temp_c * (9/5)) + 32
    return temp_f

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

print(c_to_f(temp_c))

#--------------------

def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)

print('max_sum is:', max_sum)


#-------------------
def pyramid_volume(l, w, h):
    base_area = length * width
    volume = base_area * height * (1/3)    
    return volume

length = float(input())
width = float(input())
height = float(input())
print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(length, width, height))
      

#-------------------
def mph_and_minutes_to_miles(x, y):
    return (minutes_traveled / 60) * miles_per_hour

miles_per_hour = float(input())
minutes_traveled = float(input())

print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))
      
      
      
      
      
      
      
      
      
      
      
      
      
      