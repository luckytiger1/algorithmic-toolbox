# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.insert(0, 0)
    stops.append(distance)
    # write your code here
    numRefills = 0
    currRefill = 0

    while currRefill <= len(stops) - 2:
        lastRefill = currRefill
        while currRefill <= len(stops) - 2 and (stops[currRefill+1] - stops[lastRefill] <= tank):
            currRefill += 1
        if currRefill == lastRefill:
            return -1
        if currRefill <= len(stops) - 2:
            numRefills += 1

    return numRefills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
