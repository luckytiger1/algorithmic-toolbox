# python3

# [34, 56, 11, 32, 43]

def max_pairwise_product2(numbers):
    if len(numbers) == 1:
        return numbers[0]

    max_item_1 = max(numbers)
    numbers.remove(max_item_1)
    max_item_2 = max(numbers)

    return max_item_1 * max_item_2


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
