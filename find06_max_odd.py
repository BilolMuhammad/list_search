def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    data = data
    data.sort()
    i, m = 0, 0
    while i < len(data):
        if data[i] % 2 != 0:
            m = data[i]
        i += 1
    return m


print(find_max_odd([9, 12, 3, 46, 4]))
