def FAST_MODULAR_EXPONENTATION(a,p,n):
    if p == 0:
        return 1
    if p % 2 == 0:
        t = FAST_MODULAR_EXPONENTATION(a, p/2, n)
        return (t*t) % n
    else:
        t = FAST_MODULAR_EXPONENTATION(a, (p-1)/2, n)
        return a * ((t*t) % n) % n
    
print(FAST_MODULAR_EXPONENTATION(14,3,29))


def MODULAR_EXPONENTIATION(a, b, n):
    c = 0
    d = 1
    binary_representation = bin(b)[2:]  # Convert b to binary representation
    print("binary is: ",binary_representation)
    for i in range(len(binary_representation) - 1, -1, -1):
        c = c << 1  # Multiply c by 2
        d = (d * d) % n

        if binary_representation[i] == '1':
            c = c + 1
            d = (d * a) % n

    return d

print(MODULAR_EXPONENTIATION(14,3,29))