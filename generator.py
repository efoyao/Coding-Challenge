import math


class Primes:
    """class to determine whether a number, in a specific range, is a prime number or not"""

    def __init__(self):
        # self.starting_value = starting_value
        # self.ending_value = ending_value
        pass

    @staticmethod
    def is_prime(value):
        """Returns 'True' if 'value' is a prime. False otherwise."""
        if value < 1:
            raise ValueError
        if value == 1:
            return False
        if value == 2:
            return True
        # if it's even and not 2, then it's not a prime
        if value > 2 and value % 2 == 0:
            return False

        max_divisor = int(math.floor(math.sqrt(value)))
        for num in range(3, max_divisor + 1, 2):
            if value % num == 0:
                return False
        return True

    def generate(self, starting_value, ending_value):
        """Return a list of all primes in a given range"""

        if type(starting_value) != int or type(ending_value) != int:
            raise TypeError
            quit()

        if starting_value < 1 or ending_value < 1 or starting_value == ending_value:
            raise ValueError
            quit()

        if starting_value > ending_value:
            temp = starting_value
            starting_value = ending_value
            ending_value = temp

        prime_list = []
        current_value = starting_value
        while current_value <= ending_value:
            if Primes.is_prime(current_value):
                prime_list.append(current_value)
                current_value += 1
                continue
            current_value += 1
        return prime_list


