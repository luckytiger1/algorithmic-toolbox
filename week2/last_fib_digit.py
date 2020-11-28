# Uses python3
import sys


def get_fibonacci_last_digit_naive(a):
    if a <= 1:
        return a
    f = list(range(a + 1))

    f[0] = 0
    f[1] = 1

    for i in range(2, a + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10

    return f[a]


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
