from generator import Primes

try:
    first_value = int(input("enter the first endpoint:"))
    second_value = int(input("enter the second endpoint:"))

except ValueError:
    print("Please enter valid integers for the endpoints")
    quit()

except:
    print("Please enter valid integers for the endpoints")
    quit()

if first_value < 1 or second_value < 1:
    print("Please enter positive numbers only")
    quit()

if first_value < second_value:
    starting_value, ending_value = first_value, second_value

elif first_value > second_value:
    starting_value, ending_value = second_value, first_value
else:
    print("Please enter a valid range. The endpoints cannot be equal")
    quit()

prime_instance = Primes()

print(prime_instance.generate(starting_value, ending_value))

