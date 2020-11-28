import time


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    total = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        total += current

    return 1


if __name__ == '__main__':
    n = int(input())
    now = time.time()
    print(fibonacci_sum_naive(n))
    later = time.time()
    print(int(later - now))
