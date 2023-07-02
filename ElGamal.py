from fast_modular import *
import secrets


def encryption(p, g, M, private):
    ''' 
    p: prime
    g:  primitive root
    M: message should be encrypted
    private: sender's private key
    '''
    y = FastExponentation(g, private, p)  # public key
    print(f"The public key is {p,g,y}")
    # Generate a random number between 1 and p-1
    k = secrets.randbelow(p - 1) + 1
    a = FastExponentation(g, k, p)
    b = M * FastExponentation(y, k, p)

    return a, b


def decryption(a, b, p, private):
    ''' 
    a, b: sender's encrypted message 
    p: prime
    private: sender's private key
    '''
    t = FastExponentation(a, private, p)
    s_inv = pow(t, -1, p)
    decrypted_message = (b * s_inv) % p

    return decrypted_message


def main():
    print("Welcome! This is a Encryption programme using ElGamal encryption.")
    p, g = map(int, input(
        "Please enter your private key: The format should be like [Prime,Generator]: \n").split(" "))
    M = (int(input("Now input the message: \n")))
    private_sender = int(input("Please input sender's private key: \n"))

    a, b = encryption(p, g, M, private_sender)
    print("The encrypted message is:", a, b)
    private_receiver = int(input("Please input receiver's private key: \n"))
    print("The decrypted message is:", decryption(a, b, p, private_receiver))


if __name__ == "__main__":
    main()
