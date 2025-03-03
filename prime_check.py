import math
import random

# This file contains the implementation of the prime number theorem and two primality tests.

# x = int(input("Input a number: \n"))

def prime_number_theorem(x):
    """
    Estimate the number of prime numbers less than or equal to a given number x using the Prime Number Theorem.

    素数定理、其实 只是约等于小于等于x的素数个数

    The Prime Number Theorem states that the number of prime numbers less than or equal to x is approximately x / log(x).

    Args:
        x (int): The upper limit to estimate the number of primes.

    Returns:
        int: An estimate of the number of prime numbers less than or equal to x.
    """
    # n bit
    n = int(math.log(2**x))

    return int(x / math.log(x))


def isPrime_Trial_division(x):
    """
    Check if a number is prime using trial division.

    This function determines if a given number `x` is prime by performing trial division.
    The complexity of this method is O(sqrt(n)).

    Args:
        x (int): The number to be checked for primality.

    Returns:
        bool: True if `x` is a prime number, False otherwise.

    Note:
        This function uses a brute-force approach to check for primality by dividing `x` 
        by all integers from sqrt(x) down to 1.

    https://en.wikipedia.org/wiki/Trial_division
    """
    y = math.sqrt(x)
    while y > 0:
        if y % x == 0:
            break
        else:
            y = y - 1

    return y == 1


def isPrime_Fermat(x):
    '''
    2 << x-2 means 2^(x-1)
    在这里底数为2，不是随机的
    # https://stackoverflow.com/questions/29595849/explain-a-code-to-check-primality-based-on-fermats-little-theorem
    561 1105会判断错误，都不是质数，是伪素数 Carmichael Numbers
    '''
    # return pow(2, x-1, x) == 1
    return (2 << x - 2) % x == 1    # 2^(x-1) % x == 1


if __name__ == "__main__":
    print(prime_number_theorem(5))
