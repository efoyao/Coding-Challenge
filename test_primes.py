import unittest
#import py.test
from generator import Primes


class TestPrimes(unittest.TestCase):
        
    def test_primes(self):
        """Test 'is_prime' method correctly identifies prime integers"""
        primes = Primes()
        self.assertFalse(primes.is_prime(1))
        self.assertEqual(primes.is_prime(2), True)
        self.assertEqual(primes.is_prime(3), True)
        self.assertEqual(primes.is_prime(100), False)
        self.assertEqual(primes.is_prime(55), False)
        self.assertTrue(primes.is_prime(97))

        with self.assertRaises(ValueError):
            primes.is_prime(-4)
            primes.is_prime(0)

    def test_generate(self):
        # test for ability to instantiate Primes class and use 'generate' method
        primes = Primes()
        result = primes.generate(7900, 7920)
        self.assertEqual(result, [7901, 7907, 7919])

        # Check inverse ranges
        inverse_result = primes.generate(7900, 7920)
        self.assertEqual(inverse_result, [7901, 7907, 7919])

        # Boundary Value testing
        boundary_result = primes.generate(7901, 7919)
        self.assertEqual(boundary_result, [7901, 7907, 7919])

        with self.assertRaises(ValueError):
            primes.generate(-4, -100)
            primes.generate(0, -100)

        # Verify invalid Values
        with self.assertRaises(TypeError):
            primes.generate("one", "two")
            primes.generate(True, False)
            primes.generate(4+5j, 2+2j)
            primes.generate("", "")


if __name__ == '__main__':
    unittest.main()

