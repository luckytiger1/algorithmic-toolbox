def euclidGCD(a, b):
    if b == 0:
        return a

    a %= b

    return euclidGCD(b, a)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(euclidGCD(a, b))
