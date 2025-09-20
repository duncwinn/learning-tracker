# This program says hello and asks for my name.

number_list = [1,2,3,4,5,100,99,1011]
max_number = number_list[0]

for number in number_list:
    if number > max_number:
        max_number = number
print(max_number)
'''
numbers = [5,2,5,2,2]

for ascii_count in numbers:
   # print('X' * ascii_count)
    for i in range(ascii_count):
        print('X', end='')
    print()


#nested loops
for x in range(5):
    for y in range(x+1):
        print(f'({x}, {y})')


# Shopping Cart
cart = [10,20,30]
total = 0
for item in cart:
    total += item
print('your total is ' + str(total))


cart.append('apple')
cart.append('banana')
cart.append('cherry')
print(cart)
print(cart[0])


#Car Game
car_state = ""

print("Enter a car state of 'stop' or 'start' or 'quit'")
car_state = input('>')

while car_state != "quit":
    if car_state == "start":
        print("Car started...")
    elif car_state == "stop":
        print("Car stopped...")
    else:
        print("I don't understand that...")
    car_state = input('>')
else:
    print("Game over...")







print('What is your weight?')  # Ask for their name.
weight = input('>')
print('Lb or Kg?')  # Ask for their name.
unit = input('>')
#
#if unit.upper() == 'L':
#    print (str(float(weight) * 0.45) + ' kg')    
#else:
 #   print (str(float(weight) / 0.45) + ' lbs')
###



name = 'John Smith'

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name must be less than 50 characters')
else:
    print('Name looks good!')



print('Hello, world!')
print('o------')
print('||||||')
print('*' * 10)

price = 10
print(price)

name = 'John'
age = 20
is_new = True


print('What is your name?')  # Ask for their name.
my_name = input('>')
print('It is good to meet you, ' + my_name)
color = input('What is you favorite color?')
print(my_name + ' likes ' + color)

print('what is your weight?')
weight = input('>')
print(my_name + ' weighs ' + weight + ' pounds and ' + str(int(weight) * 0.45) + ' kilograms')

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
msg = f'{first} [{last}] is a coder'
print(msg)

course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)  #true or false - case sensitive
print(course.title())
print(course.strip())
print(course.split())
print(course.find('for'))
print(course.replace('for', '4'))



print('The length of your name is:')
print(len(my_name))
print('What is your age?')  # Ask for their age.
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
'''