import unittest

class PrintPrimeNumbersInArange(unittest.TestCase):

def test_if_num_is_less_than_zero(self):
"""test if number is less than zero"""
 self.asserTrue(num<0,"Do not print number")

def test_is_prime_number_within_range(self):
"""all printed numbers should be within the given range"""
   self.assertTrue(n<num>0,"Do not print number")

def test_if_number_is_divisible_by_two_and_numberis_not_two(self):
	"""test if number is divisible by 2 and the number is not two"""
	self.assertTrue(num%2==0 and num!=2,"Do not print number")

def test_if_number_is_divisible_by_three_and_number_not_three(self):

    """test if number is divisible by three and the number is not three"""

    self.assertTrue(num%3==0 and num!=3,"Do not Print Number")


def test_if_number_is_a_whole_number(self):

    """test if number is a whole number and not a decimal or fraction"""

    self.asserEqual(if (num is a whole number),"Print Number" )
 
def test_if_number_is_zero(self):

     """if number is zero, give error message""" 

     self.asserEqual(0,"Do not print Zero")
     

def test_if_number_is_one(self):


     	"""If number is One, give error message"""

     	self.asserEqual(1,"Do not print 1")


def test_if_number_is_Two(self):

     		"""2 is a prime number"""

     		self.asserEqual(2,"Print 2")


def test_if_number_is_Three(self):

     		"""3 is a prime number"""

     		self.asserEqual(3,"Print 3")

def test_if_number_on_upper_range_is_prime(self):

	self.assertTrue(True,"Print number")




     		if __name__ == '__main__':
    unittest.main()

