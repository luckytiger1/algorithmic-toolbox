# Uses python3
import sys
import math


def get_change(m):
    min_coins = []
    for k in range(m + 1):
        min_coins.append(0)
    coins = [1, 3, 4]
    min_coins[0] = 0
    for i in range(1, m + 1):
        min_coins[i] = math.inf
        for j in coins:
            if i >= j:
                num_coins = min_coins[i - j] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    return min_coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
