import math
import random


def isPrime_Witness(x, k=5):
    '''
    # https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/
    '''
    if x < 2 or (x != 2 and x % 2 == 0):
        return False
    if x == 2 or x == 3:
        return True

    # 将 x - 1 表示为 (2^t) * d 的形式
    t = 0
    d = x - 1
    while d % 2 == 0:
        t += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, x-2)
        y = pow(a, d, x)

        if y == 1 or y == x-1:
            continue
        for _ in range(t - 1):
            y = pow(y, 2, x)  # 计算 x^2 mod n
            if y == x - 1:
                break

        else:
            return False

    return True


def isComposite_rabin_miller(x, kk=5):
    """
    使用Rabin-Miller算法测试一个数是否为合数。

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

    # 将 x - 1 表示为 (2^k) * m 的形式
    k = 0
    m = x - 1
    while m % 2 == 0:
        k += 1
        m //= 2

    for _ in range(kk):
        a = random.randint(2, x - 2)
        y = pow(a, m, x)

        if y == 1 or y == x - 1:
            continue

        for _ in range(k - 1):
            y = pow(y, 2, x)  # 计算 y^2 mod x
            if y == x - 1:
                break
        else:
            return True

    return False


if __name__ == "__main__":
    x = int(input("Input a number: \n"))
    print("is Composite?",isComposite_rabin_miller(x))
    print("is prime?",isPrime_Witness(x))