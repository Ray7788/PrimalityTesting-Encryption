# Primality Testing and Encryption🔒
The [El Gamal encryption](https://en.wikipedia.org/wiki/ElGamal_encryption) system is a public-key cryptography asymmetric key encryption scheme based on the Diffie-Hellman key exchange. Taher Elgamal described it in 1985. ElGamal encryption is used in GNU Privacy Guard, newer versions of PGP, and other cryptosystems. 

A one-way function is one that is easy to compute but hard to invert. Formally, a function is one-way if it can be computed in polynomial time but any polynomial time randomised algorithm that attempts to compute a pseudo-inverse for succeeds with negligible probability.

Here is the one-way function for The El Gamal encryption:
![image](https://github.com/Ray7788/PrimalityTesting-Encryption/assets/87214670/6bd85df1-d4b1-4afc-86f8-b4a7f3285978)

The **greatest common divisor**, [(gcd)](gcd.py), or highest common factor, hcf, of two numbers is largest integer that divides them both, which is utilized for the "mod" operation.

To encrypt a message using El Gamal Encryption. You need to find a random which is relatively **prime** [using bsaic primality testing methods](prime_check.py) or [Rabin Miller method](Rabin_Miller.py) to (where is a prime appearing in the public key) and then compute for various numbers. 
In order to do this you will need to use a [**FAST MODULAR EXPONENTIATION**](fast_modular.py) algorithm.
