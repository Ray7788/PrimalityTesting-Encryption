# Primality Testing and Encryption🔒 质数（素数）检测与加密算法
English
====
The [El Gamal encryption](https://en.wikipedia.org/wiki/ElGamal_encryption) system is a public-key cryptography asymmetric key encryption scheme based on the Diffie-Hellman key exchange. Taher Elgamal described it in 1985. ElGamal encryption is used in GNU Privacy Guard, newer versions of PGP, and other cryptosystems. 

A one-way function is one that is easy to compute but hard to invert. Formally, a function is one-way if it can be computed in polynomial time but any polynomial time randomised algorithm that attempts to compute a pseudo-inverse for succeeds with negligible probability.

Here is the one-way function for The El Gamal encryption:
![image](https://github.com/Ray7788/PrimalityTesting-Encryption/assets/87214670/6bd85df1-d4b1-4afc-86f8-b4a7f3285978)

The **greatest common divisor**, [(gcd)](gcd.py), or highest common factor, hcf, of two numbers is largest integer that divides them both, which is utilized for the "mod" operation.

To encrypt a message using El Gamal Encryption. You need to find a random which is relatively **prime** using some [basic primality testing](prime_check.py) methods or [Rabin Miller](Rabin_Miller.py) method to (where is a prime appearing in the public key) and then compute for various numbers. 
In order to do this you will need to use a [**FAST MODULAR EXPONENTIATION**](fast_modular.py) algorithm.

----------------
简体中文
====
在密码学中，ElGamal加密算法是一个基于迪菲-赫尔曼密钥交换的非对称加密算法。它在1985年由塔希尔·盖莫尔提出。[1]GnuPG和PGP等很多密码学系统中都应用到了ElGamal算法。

单向函数是一个容易计算但很难反转的函数。从形式上看，如果一个函数可以在多项式时间内被计算出来，但任何试图计算其伪逆的多项式时间随机算法都会以可忽略的概率成功。

这里是El Gamal加密的单向函数：
![image](https://github.com/Ray7788/PrimalityTesting-Encryption/assets/87214670/6bd85df1-d4b1-4afc-86f8-b4a7f3285978)

两个数字的最大公因数，[(gcd)](gcd.py)，或最高公因数，hcf，是两个数字相除的最大整数，用于 "mod "操作。

使用El Gamal加密法对信息进行加密。你需要使用一些[基本素数检测，比如素数定理，暴力测试，费马小定理](prim_check.py)方法或[Rabin Miller](Rabin_Miller.py)方法找到一个**互质的随机数**（其中素数出现在公钥中），然后对各种数字进行计算。
为了做到这一点，你需要使用[快速模幂解析](fast_modular.py)算法。
