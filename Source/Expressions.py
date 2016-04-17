from __future__ import division
import random
import calendar, time

# Seed the PRNG
random.seed(calendar.timegm(time.gmtime()))

# Fractional constants
FRAC_NUMERATOR_MIN = 1
FRAC_NUMERATOR_MAX = 6
FRAC_DENOMINATOR_MIN = 2
FRAC_DENOMINATOR_MAX = 11
FRAC_MULTIPLE_MIN = 1
FRAC_MULTIPLE_MAX = 3
FRAC_CHANCE_SIMPLIFIED = 0.2
FRAC_CHANCE_IMPROPER = 0.4

def get_gcd(num1, num2):
    """
    Gets the greatest common divisor of two numbers.

    :param num1: The first number.
    :param num2: The second number.
    :return: The GCD.
    """
    if (num2 == 0):
        return num1
    return get_gcd(num2, num1 % num2)

class Fraction:
    """
    Defines a representation for a fraction.
    """
    numerator = 0
    denominator = 0

    def __init__(self, num = 1, denom = 1):
        """
        Creates a new fraction.

        :param num: The fraction's numerator.
        :param denom: The fraction's denominator.
        """
        self.numerator = num
        self.denominator = denom

    def can_be_reduced(self):
        """
        Checks to see if this fraction can be reduced.

        :return: True if this fraction can be reduced, False if not.
        """
        return get_gcd(self.numerator, self.denominator) > 1

    def get_common_factors(self):
        """
        Gets all of the common factors of the numerator and the denominator.

        :return: The list of common factors.
        """
        factors = []
        for x in range(2, max(self.numerator, self.denominator)):
            if (self.numerator % x == 0 and self.denominator % x == 0):
                factors.append(x)
        return factors

    def get_equal_fraction(self):
        """
        Gets a fraction equal to this one.

        :return: An equal fraction.
        """
        multiple = random.randint(FRAC_MULTIPLE_MIN, FRAC_MULTIPLE_MAX)
        if (random.random() < FRAC_CHANCE_SIMPLIFIED):
            factors = self.get_common_factors()
            if (len(factors) > 0):
                index = random.randint(0, len(factors) - 1)
                multiple = 1 / factors[index]
        return Fraction(int(self.numerator * multiple), int(self.denominator * multiple))

    def __str__(self):
        """
        Gets this fraction as a string.

        :return: The string representation of this fraction.
        """
        if (self.denominator == 1):
            return str(self.numerator)
        return "{0}/{1}".format(self.numerator, self.denominator)

def frac_random_numerator():
    """
    Gets a random numerator for a fraction.

    :return: The random numerator.
    """
    return random.randint(FRAC_NUMERATOR_MIN, FRAC_NUMERATOR_MAX)

def frac_random_denominator():
    """
    Gets a random denominator for a fraction.

    :return: The random denominator.
    """
    return random.randint(FRAC_DENOMINATOR_MIN, FRAC_DENOMINATOR_MAX)

def frac_random():
    """
    Creates a random fraction.

    :return: The random fraction.
    """
    num = frac_random_numerator()
    denom = frac_random_denominator()
    if (random.random() < FRAC_CHANCE_IMPROPER):
        while (denom >= num and denom == 1):
            num = frac_random_denominator()
            denom = frac_random_numerator()
    else:
        while (num >= denom):
            denom = frac_random_denominator()
    return Fraction(num, denom)
