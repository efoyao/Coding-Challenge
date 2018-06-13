from generator import Primes

first_value = input("enter the first endpoint:")
second_value = input("enter the second endpoint:")

try:
    first_value = int(first_value)
    second_value = int(second_value)
except ValueError:
    print("Please enter valid integers for the endpoints")

if first_value < 1:
    print("Please enter positive numbers only")
if second_value < 1:
    print("Please enter positive numbers only")

if first_value < second_value:
    starting_value, ending_value = first_value, second_value

elif first_value > second_value:
    starting_value, ending_value = second_value, first_value
else:
    print("Please enter a valid range. The endpoints cannot be equal")

prime_instance = Primes()

print(prime_instance.generate(starting_value, ending_value))

