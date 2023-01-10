def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i, min = 0, 0
    data = data
    data.sort(reverse=True)
    while i < len(data):
        if data[i] % 2 != 0:
            min = data[i]
        i += 1
    if min == 0:
        return -1

    return min


print(find_min_odd([2, 4, 5, 7, 9]))
