from Rabin_Miller import *

# 快速模幂算法 Fast Exponentiation
# This file contains the implementation of the Fast Exponentiation algorithm by both squaring and binary method.


def FastExponentation(a, p, n):
    """
    Computes a^p mod n using the method of exponentiation by squaring.

    Parameters:
    a (int): The base.
    p (int): The exponent.
    n (int): The modulus.

    Returns:
    int: The result of a^p mod n.

    Examples:
    >>> FastExponentation(2, 10, 1000)
    24
    >>> FastExponentation(3, 5, 13)
    5
    """
    if p == 0:
        return 1
    if p % 2 == 0:
        t = FastExponentation(a, p // 2, n)
        return (t * t) % n
    else:
        t = FastExponentation(a, (p - 1) // 2, n)
        return (a * t * t) % n


def MODULAR_EXPONENTIATION(a, b, n):
    """
    Perform modular exponentiation using the binary method.

    This function calculates (a^b) % n using an efficient method that 
    leverages the binary representation of the exponent.

    Parameters:
    a (int): The base.
    b (int): The exponent.
    n (int): The modulus.

    Returns:
    int: The result of (a^b) % n.
    """
    c = 0
    d = 1
    binary_representation = bin(b)[2:]  # Convert b to binary representation
    print("The binary representation is ", binary_representation)
    for i in range(len(binary_representation) - 1, -1, -1):
        c = c << 1  # Multiply c by 2
        d = (d * d) % n

        if binary_representation[i] == '1':
            c = c + 1
            d = (d * a) % n

    return d


if __name__ == "__main__":
    print(FastExponentation(14, 3, 29))
    print(MODULAR_EXPONENTIATION(14, 3, 29))
