import unittest
from Prime import Prime

class TestPrime(unittest.TestCase):
    def test_prime(self):
        prime_instance = Prime()
        prime_instance.prime()
        self.assertEqual(prime_instance.P, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                                             31, 37, 41, 43, 47, 53, 59, 
                                             61, 67, 71, 73, 79, 83, 89, 97])

if __name__ == '__main__':
    unittest.main()