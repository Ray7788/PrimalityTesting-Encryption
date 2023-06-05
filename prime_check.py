import math, random

# x = int(input("Input a number: \n"))

def prime_number_theorem(x):
    ''' 
    素数定理、其实 只是约等于小于等于x的素数个数

    '''
    # n bit
    n = int(math.log(2**x))

    return int(x / math.log(x))

def isPrime_Trial_division(x):
    '''
    暴力测试 复杂度O(n**0.5)
    # https://en.wikipedia.org/wiki/Trial_division
    '''
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
    return (2 << x - 2) % x == 1

print(prime_number_theorem(5))