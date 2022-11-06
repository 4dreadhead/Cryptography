from math import gcd


class CipherMath:
    @classmethod
    def mod_exp(cls, base=0, exp=0, mod=1, use_builtin_function=True):
        if use_builtin_function:
            return pow(base, exp, mod)

        result = 1
        while exp:
            if exp & 1:
                result = result * base % mod
            exp >>= 1
            base = base ** 2 % mod

        return result

    @classmethod
    def gcd(cls, a=1, b=1, use_builtin_function=True):
        if use_builtin_function:
            return gcd(a, b)

        while b:
            a, b = b, a % b
        return a

    @classmethod
    def mod_inv(cls, base=0, mod=1, use_builtin_function=True):
        if use_builtin_function:
            pow(base, -1, mod)

        if cls.gcd(base, mod) != 1:
            raise ValueError("base is not invertible for the given modulus")

        for num in range(1, mod+1):
            if (num * base) % mod == 1:
                return num

        return None
