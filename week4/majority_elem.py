# Uses python3
import sys


def get_majority_element(arr, left, right):
    if left == right:
        return -1

    def majority_element(lo, hi):
        if lo == hi:
            return arr[lo]

        mid = lo + (hi - lo) // 2
        leftSide = majority_element(lo, mid)
        rightSide = majority_element(mid + 1, hi)

        if leftSide == rightSide:
            return rightSide

        left_c = sum(1 for i in range(lo, hi + 1) if arr[i] == leftSide)
        right_c = sum(1 for i in range(lo, hi + 1) if arr[i] == rightSide)

        if left_c > right_c:
            return leftSide
        else:
            return rightSide

    return majority_element(0, right - 1)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    totalCount = sum(1 for i in range(n-1) if a[i] == get_majority_element(a, 0, n))
    if totalCount > n // 2:
        print(1)
    else:
        print(0)
