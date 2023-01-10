def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """

    i, min = 0, 0
    data = data
    data.sort(reversed=True)
    while i < len(data):
        if data[i] % 2 == 0:
            min = data[i]
        i += 1
    if min == 0:
        return -1
    return min
