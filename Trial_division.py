import math, random

x = int(input("Input a number: \n"))

def isPrime_Trial_division(x):
    '''
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
    2 << x-2  means 2^(x-1)
    # https://stackoverflow.com/questions/29595849/explain-a-code-to-check-primality-based-on-fermats-little-theorem
    '''
    # return pow(2, x-1, x) == 1
    return (2 << x - 2) % x == 1

def isPrime_Witness(x, k=5):
    '''
    # https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
    '''
    if x < 2 or (x != 2 and x%2 == 0):
        return False
    if x ==2 or x==3:
        return True
    
    # 将 x - 1 表示为 (2^r) * d 的形式
    t = 0
    d = x - 1
    while d % 2 == 0:
        t += 1
        d //= 2
    
    for _ in range(k):
        a = random.randint(2, x-2)
        y = pow(a,d,x)

        if y == 1 or y == x-1:
            continue
        for _ in range(t - 1):
            y = pow(y, 2, x)  # 计算 x^2 mod n
            if y == x - 1:
                break

        else:
            return False
        
    return True


def isComposite_rabin_miller(x, k=5):
    """使用Rabin-Miller算法测试一个数是否为合数。

    参数：
    x -- 待测试的数
    k -- 进行测试的次数（可选，默认为5）

    返回值：
    如果 x 是合数，则返回 True，否则返回 False。
    """

    if x < 2 or (x != 2 and x % 2 == 0):
        return True
    if x == 2 or x == 3:
        return False

    # 将 x - 1 表示为 (2^t) * d 的形式
    t = 0
    d = x - 1
    while d % 2 == 0:
        t += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, x - 2)
        y = pow(a, d, x)
        temp = d

        if y == 1 or y == x - 1:
            continue

        for _ in range(t - 1):
            y = pow(y, 2, x)  # 计算 y^2 mod x
            if y == x - 1:
                break
        else:
            return True

    return False



print(isPrime_Witness(x))