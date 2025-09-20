import math

print(math.ceil(2.9))
print(math.floor(2.9))
print(math.pi)
print(math.e)
print(math.sqrt(144))
print(math.factorial(5))
print(math.sin(math.pi/2))
print(math.cos(math.pi/2))
print(math.tan(math.pi/2))

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear a jacket")
else:
    print("It's a lovely day")

house_price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = house_price * 0.1
else:
    down_payment = house_price * 0.2

print(f"Down payment: ${down_payment}")