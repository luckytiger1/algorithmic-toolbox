import sys


def get_optimal_value(capacity, weights, values):
    value = 0.

    for n in range(len(values)):
        if capacity == 0:
            return value
        p = []
        for i in range(len(weights)):
            if weights[i] > 0:
                p.append(values[i]/weights[i])

        i = max(p)
        a = min(weights[p.index(i)], capacity)
        value = value + a * (values[p.index(i)]/weights[p.index(i)])
        weights[p.index(i)] -= a
        capacity -= a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
