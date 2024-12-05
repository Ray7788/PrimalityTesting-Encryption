from Rabin_Miller import isComposite_rabin_miller
from gcd import gcd
from fast_modular import MODULAR_EXPONENTIATION
import random

def mod_inverse(a, m):
    """
    Calculate the modular multiplicative inverse of a modulo m.

    Parameters:
    a (int): The number whose inverse is to be calculated.
    m (int): The modulus.

    Returns:
    int: The modular multiplicative inverse of a modulo m.
    """
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process same as Euclid's Algorithm
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x = x + m0

    return x


def create_prime_nums(keylength, times=10):
    """
    Create two distinct prime numbers of the given key length.

    Parameters:
    keylength (int): The length of the prime numbers to be generated.

    Returns:
    tuple: A tuple containing two distinct prime numbers.
    """
    primes = set()
    while len(primes) < 2:
        n = random.getrandbits(keylength)
        if n % 2 != 0:
            prime_found = True
            for _ in range(0, times):
                if not isComposite_rabin_miller(n):
                    pass
                else:
                    prime_found = False
                    break
            if prime_found:
                primes.add(n)
    return tuple(primes)


def generate_keypair(keylength):
    """
    Generate a pair of public and private keys.

    Parameters:
    keylength (int): The length of the key to be generated.

    Returns:
    tuple: A tuple containing the public and private keys: ((e, n), (d, n)).
    (e, n) is the public key, and (d, n) is the private key.
    """
    p, q = create_prime_nums(keylength)
    n = p * q
    phi = (p - 1) * (q - 1)  # Euler's Totient function

    # Choose an integer e such that 1 < e < phi, and e is coprime to phi.
    e = random.randint(2, phi - 1)
    while True:
        # Check if two numbers are coprime.
        if gcd(e, phi) == 1:
            break
        e = random.randint(1, phi)

    # Use the Extended Euclidean Algorithm to generate the private key.
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))


def mod_inverse(a, m):
    """
    Calculate the modular multiplicative inverse of a modulo m.

    Parameters:
    a (int): The number whose inverse is to be calculated.
    m (int): The modulus.

    Returns:
    int: The modular multiplicative inverse of a modulo m.
    """
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process same as Euclid's Algorithm
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x = x + m0

    return x

def encrypt(public_key, plaintext):
    """
    Encrypt a plaintext message using the public key.

    Parameters:
    public_key (tuple): The public key (e, n).
    plaintext (int): The plaintext message to be encrypted.

    Returns:
    int: The encrypted ciphertext.
    """
    e, n = public_key
    return MODULAR_EXPONENTIATION(plaintext, e, n)

def decrypt(private_key, ciphertext):
    """
    Decrypt a ciphertext message using the private key.

    Parameters:
    private_key (tuple): The private key (d, n).
    ciphertext (int): The ciphertext message to be decrypted.

    Returns:
    int: The decrypted plaintext.
    """
    d, n = private_key
    return MODULAR_EXPONENTIATION(ciphertext, d, n)

def display():
    print("_________________RSA_________________")
    print("1.encrypt")
    print("2.decrypt")
    print("q.quit")
    print("Enter the key you wanna try")
    print("_____________________________________")

def main():
    print("Welcome! This is a RSA encryption programme.")
    keylength = int(input("Please enter the key length: \n"))
    public, private = generate_keypair(keylength)
    print(f"Public key: {public}")
    print(f"Private key: {private}")
    while True:
        display()
        key = input()
        if key == '1':
            plaintext = int(input("Please enter the plaintext message: \n"))
            print("The encrypted message is:", encrypt(public, plaintext))
        elif key == '2':
            ciphertext = int(input("Please enter the ciphertext message: \n"))
            print("The decrypted message is:", decrypt(private, ciphertext))
        elif key == 'q':
            break
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    main()

"""
A test sanple:
Input: 5
Output:
Welcome! This is a RSA encryption programme.
Please enter the key length:
Public key: ((5, 35), (29, 35))
Private key: ((29, 35), (5, 35))
_________________RSA_________________

"""