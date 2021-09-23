# recursion functions
def factorial(n: int):
    """
    calculate factorial of n number
    :param n:
    :return:
    """
    assert n >= 0, "negative factorial not recognized"
    if n == 0:
        return 1
    return factorial(n - 1) * n  # product by n after back from recursion function


#  Euclidean Algorithm
def gcd(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    # --- version 1 ---
    # if a == b:
    #     return a
    # elif a > b:
    #     return gcd(a - b, b)
    # else:  # a < b
    #     return gcd(a, b - a)

    # --- version 2 ---
    # if b == 0:
    #     return a
    # else:  # a < b
    #     return gcd(b, a%b)

    # --- version 3 ---
    return a if b == 0 else gcd(b, a % b)


def quick_pow(a: float, num: int):
    # return 1 if num == 0 else quick_pow(a, num - 1) * a

    # version 2
    if num == 0:
        return 1
    elif num % 2 == 1:
        return pow(a, num - 1) * a
    else:
        return pow(a ** 2, num // 2)
