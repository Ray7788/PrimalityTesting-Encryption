"""
欧几里得算法
The greatest common divisor, gcd, or highest
common factor, hcf, of two numbers is largest
integer that divides them both.

• If gcd(a, b) = 1(or hcf(a, b) = 1) we say that a and b are relatively prime.
"""


def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of the two integers.

    Prints:
        str: A message indicating that the integer 'a' has a multiplicative inverse in Zn if the GCD is 1.
    """
    if b == 0:
        if a == 1:
            print("iff", a, "has a multiplicative inverse in Zn")
        return a
    else:
        r = a % b
        return gcd(b, r)


if __name__ == "__main__":
    print("Please enter 2 numbers (number1 > number2) to check the greatest common divisor")
    x = int(input("Input a number1: \n"))
    y = int(input("Input a number2: \n"))
    print(gcd(x, y))
