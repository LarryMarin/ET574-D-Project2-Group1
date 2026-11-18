import unittest
from my_math import fibonacci, mean, divisors, sqrt

class TestMyMath(unittest.TestCase):
    # ----- fibonacci-----
    # test if the fabonacci() returns expected values
    # i.e. fibonacci(0) = 0, fibonacci(1)= 1, ..., fibonacci(6)= 8
    def test_fibonacci_basic(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(6), 8)

    # test if an invalid value passed in will raise either an error  
    def test_fibonacci_bad_inputs(self):
        #test if error will raise when a negative number (-1) is passed in
        with self.assertRaises((TypeError, ValueError)):
            fibonacci(-1)

     	#test if error will raise when a float number (3.5) is passed in
        with self.assertRaises((TypeError, ValueError)):
            fibonacci(3.5)        

        #test if error will raise when an invalid type (string "7") is passed in
        with self.assertRaises((TypeError, ValueError)):
            fibonacci("7") 

    # test if the Fibonacci rule is implemented correctly: F(n) = F(n-1) + F(n-2), for n >= 2
    def test_fibonacci_relation(self):
        self.assertEqual(fibonacci(7), fibonacci(6) + fibonacci(5))
        self.assertEqual(fibonacci(10), fibonacci(9) + fibonacci(8))       

    # ----- mean -----
    # test if the mean of a group of numbers passed in will return an expected result
    # use assertAlmostEqual() when comparing float numbers.
    def test_mean_basic(self):
        #the mean of numbers 1,2,3 is 2.0
        self.assertAlmostEqual(mean([1, 2, 3]), 2.0)

	#the mean of two numbers 1.5 and 2.5 is 2.0
        self.assertAlmostEqual(mean([1.5, 2.5]), 2.0)

        #the mean of four 0's is 0
        self.assertAlmostEqual(mean([0, 0, 0, 0]), 0.0)

    #test special cases
    def test_mean_singleton_and_mixed(self):
        #the mean of one number passed should be itself
        self.assertAlmostEqual(mean([42]), 42.0)
        #the mean of integer and float numbers mixed, i.e. 1, 2.0 and 3, should be 2.0.
        self.assertAlmostEqual(mean([1, 2.0, 3]), 2.0)

    #test error handles
    def test_mean_errors(self):
        #test if error will raise if no number is passed in.
        with self.assertRaises((ValueError, ZeroDivisionError)):
            mean([])
        #test if error will raise if an invalid data type (string "two") is passed in.
        with self.assertRaises((TypeError, ValueError)):
            mean([1, "two", 3])  

    # ----- divisors -----
    #Larry's test cases
    # test if divisors() returns the expected list for a positive integer
    def test_divisors_basic(self):
        self.assertEqual(divisors(12), [1, 2, 3, 4, 6, 12])

    # test if an error is raised when 0 is passed in
    def test_divisors_zero(self):
        with self.assertRaises(ValueError):
            divisors(0)

    # ----- sqrt -----
    #Larry's test cases
    # test if sqrt() returns the expected values for typical inputs
    # use assertAlmostEqual() because the results are floats
    def test_sqrt_basic(self):
        self.assertAlmostEqual(sqrt(25), 5.0)
        self.assertAlmostEqual(sqrt(2.25), 1.5)

    # test the edge case: the square root of 0 is 0.0
    def test_sqrt_zero(self):
        self.assertAlmostEqual(sqrt(0), 0.0)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
