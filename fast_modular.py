from Rabin_Miller import *

# 快速模幂算法
def FastExponentation(a, p, n):
    ''' 
    a^p mod n

    a: Base
    P: Exponent
    n: Modulus
    '''
    try:
        return isPrime_Witness(p)
    except:
        print("error!")
    else:
        if not isPrime_Witness(n):
            return 
        if p == 0:
            return 1
        if p % 2 == 0:
            t = FastExponentation(a, p // 2, n)
            return (t*t) % n
        else:
            t = FastExponentation(a, (p-1) // 2, n)
            return a * ((t*t) % n) % n


def MODULAR_EXPONENTIATION(a, b, n):
    ''' 
    a^b mod n

    a: Base
    b: Exponent
    n: Modulus
    '''
    c = 0
    d = 1
    binary_representation = bin(b)[2:]  # Convert b to binary representation
    print("binary is: ", binary_representation)
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
