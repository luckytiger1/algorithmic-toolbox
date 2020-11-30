# Uses python3
import sys
import math


def binary_search(a, x):
    left, right = 0, len(a) - 1

    return b_search(a, left, right, x)


def b_search(a, low, high, key):
    if high < low:
        return  -1

    mid = math.floor(low + (high - low) / 2)

    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return b_search(a, low, mid - 1, key)
    else:
        return b_search(a, mid + 1, high, key)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
