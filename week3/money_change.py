def get_change(n):
    if n <= 1:
        return 1

    k = 0
    b = 0
    v = 0
    if n % 10 == 0:
        return int(n / 10)
    else:
        if n > 10:
            k = int(n / 10)
            if n % 10 >= 5:
                b = int(n % 10 / 5)
                if n % 10 / 5 != 0:
                    v = n % 10 % 5
            else:
                v = n % 10
        else:
            if n > 5:
                b = int(n / 5)
                v = n % 5
            else:
                v = n % 5

    return k + b + v


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
